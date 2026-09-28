from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from .choices import SOCIAL_PLATFORM_CHOICES, TRAIT_TYPE_CHOICES, FILE_TYPE_CHOICES


class TraitStructValue(blocks.StructValue):
    def trait_type_display(self):
        return dict(TRAIT_TYPE_CHOICES).get(self.get('trait_type'), '')


class AssetDownloadStructValue(blocks.StructValue):
    def file_type_display(self):
        return dict(FILE_TYPE_CHOICES).get(self.get('file_type'), '')


class SocialLinkBlock(blocks.StructBlock):
    platform = blocks.ChoiceBlock(choices=SOCIAL_PLATFORM_CHOICES)
    url = blocks.URLBlock()

    class Meta:
        template = "blocks/social_link_block.html"
        icon = "link"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['platform_label'] = dict(SOCIAL_PLATFORM_CHOICES).get(value.get('platform'), value.get('platform'))
        return context


class TraitBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    trait_type = blocks.ChoiceBlock(choices=TRAIT_TYPE_CHOICES)
    description = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        template = "blocks/trait_block.html"
        icon = "image"
        value_class = TraitStructValue


class AssetDownloadBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    file_type = blocks.ChoiceBlock(choices=FILE_TYPE_CHOICES)
    file = DocumentChooserBlock(required=False)

    class Meta:
        template = "blocks/asset_download_block.html"
        icon = "download"
        value_class = AssetDownloadStructValue