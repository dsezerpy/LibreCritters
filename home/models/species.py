from django.db import models
from django.conf import settings
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from .blocks import SocialLinkBlock, TraitBlock, AssetDownloadBlock
from .choices import LICENSE_CHOICES


class SpeciesPageTag(TaggedItemBase):
    content_object = ParentalKey('SpeciesPage', on_delete=models.CASCADE, related_name='tagged_items')


class SpeciesPage(Page):
    subpage_types = []

    creator_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_species',
        help_text="Registered platform user who created this species."
    )
    creator_name = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text="Display name if the creator is external or not a registered user."
    )

    tags = ClusterTaggableManager(through=SpeciesPageTag, blank=True)
    is_featured = models.BooleanField(default=False, help_text="Pin to curated showcases.")
    has_content_warning = models.BooleanField(default=False, help_text="Flag for mature themes/body horror.")

    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Main preview banner for home grid and header."
    )
    parent_species = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='forks',
        help_text="Select if this species is a fork/derivative of another species on LibreCritters."
    )
    has_oc_exemption = models.BooleanField(
        default=True,
        help_text="Displays the '100% Exclusive Character Copyright' protection badge on the page."
    )
    description = RichTextField(
        blank=True,
        help_text="Species lore, baseline guidelines, and design rules."
    )
    traits = StreamField([
        ('trait', TraitBlock()),
    ], blank=True, use_json_field=True, help_text="Modular anatomical specs and trait breakdowns.")

    license_type = models.CharField(
        max_length=20,
        choices=LICENSE_CHOICES,
        default='CC_BY_SA',
        help_text="Copyleft license applied to this species."
    )
    asset_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Primary downloadable PSD/vector source file."
    )
    additional_assets = StreamField([
        ('asset', AssetDownloadBlock()),
    ], blank=True, use_json_field=True, help_text="Extra community assets, 3D models, lineart, etc.")

    creator_socials = StreamField([
        ('social', SocialLinkBlock()),
    ], blank=True, use_json_field=True)

    # Search Configuration
    search_fields = Page.search_fields + [
        index.SearchField('creator_name'),
        index.SearchField('description'),
        index.FilterField('license_type'),
        index.FilterField('is_featured'),
    ]

    # Panel Layout
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('creator_user'),
            FieldPanel('creator_name'),
            FieldPanel('creator_socials'),
        ], heading="Creator Attribution"),
        FieldPanel('cover_image'),
        FieldPanel('tags'),
        MultiFieldPanel([
            FieldPanel('parent_species'),
            FieldPanel('is_featured'),
            FieldPanel('has_content_warning'),
        ], heading="Specification Metadata & Lineage"),
        FieldPanel('description'),
        FieldPanel('traits'),
        MultiFieldPanel([
            FieldPanel('license_type'),
            FieldPanel('has_oc_exemption'),
            FieldPanel('asset_file'),
            FieldPanel('additional_assets'),
        ], heading="Licensing & Source Assets"),
    ]

    @property
    def show_ads(self):
        return "NC" not in self.license_type

    @property
    def species_type(self):
        if self.license_type in ['CLOSED']:
            return 'Closed'
        elif self.license_type in ['CC_BY', 'CC_BY_SA']:
            return 'Libre'
        elif self.license_type == 'CC0':
            return 'Public Domain'
        else:
            return 'Open'

    @property
    def short_license(self):
        license_map = {
            'CC0': 'CC0 1.0',
            'CC_BY': 'CC BY 4.0',
            'CC_BY_SA': 'CC BY-SA 4.0',
            'CC_BY_NC': 'CC BY-NC 4.0',
            'CC_BY_NC_SA': 'CC BY-NC-SA 4.0',
            'CC_BY_ND': 'CC BY-ND 4.0',
            'CC_BY_NC_ND': 'CC BY-NC-ND 4.0',
            'OPEN': 'Open / Unlicensed',
            'CLOSED': 'Closed',
        }
        return license_map.get(self.license_type, self.license_type)

    @property
    def display_creator(self):
        if self.creator_user:
            return self.creator_user.get_full_name() or self.creator_user.username
        return self.creator_name or "Anonymous"