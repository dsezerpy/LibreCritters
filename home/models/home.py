from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from .species import SpeciesPage


class HomePage(Page):
    """The landing page for LibreCritters."""
    
    intro = RichTextField(
        blank=True, 
        help_text="Welcome text and mission statement for the homepage."
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['species_list'] = SpeciesPage.objects.live().public().order_by('-is_featured', '-first_published_at')[
            :6]
        return context