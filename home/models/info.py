from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel


class InfoPage(Page):
    """A generic flexible page for standard text-heavy content."""
    
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title", icon="title")),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]