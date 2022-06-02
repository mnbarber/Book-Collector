from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Author

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Author:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

authors = [
    Author("Sarah J Maas", "https://sarahjmaas.com/wp-content/uploads/2021/08/Sarah-headshot-color-med.jpg", "Sarah J. Maas is the #1 New York Times and internationally bestselling author of the Throne of Glass, Court of Thorns and Roses, and Crescent City series. Her books have sold millions of copies and are published in thirty-seven languages."),
    Author("Leigh Bardugo", "https://www.leighbardugo.com/wp-content/uploads/2018/05/0138-leigh-bardugo-%C2%A9jencastlephotography_edit-1200x1595.jpg", "Leigh Bardugo is a #1 New York Times bestselling author of fantasy novels and the creator of the Grishaverse (now a Netflix original series) which spans the Shadow and Bone Trilogy, the Six of Crows Duology, The Language of Thorns, and King of Scars—with more to come. Her short stories can be found in multiple anthologies, including the Best American Science Fiction & Fantasy. Her other works include Wonder Woman: Warbringer and Ninth House (Goodreads Choice Winner for Best Fantasy 2019) which is being developed for television by Amazon Studios. She lives in Los Angeles."),
    Author("Cassandra Clare", "https://cassandraclare.com/wp-content/uploads/2020/01/cassandraclare.jpg", "Cassandra Clare was born to American parents in Teheran, Iran and started working on her YA novel, City of Bones, in 2004. Cassie hates working at home alone because she always gets distracted by reality TV shows and the antics of her two cats, so she usually sets out to write in local coffee shops and restaurants. She likes to work in the company of her friends, who see that she sticks to her deadlines."),
    Author("Stephen King", "https://stephenking.com/images/press/stephenking-sm.jpg", "Stephen King was born in Portland, Maine in 1947, the second son of Donald and Nellie Ruth Pillsbury King. He made his first professional short story sale in 1967 to Startling Mystery Stories. In the fall of 1971, he began teaching high school English classes at Hampden Academy, the public high school in Hampden, Maine. Writing in the evenings and on the weekends, he continued to produce short stories and to work on novels. In the spring of 1973, Doubleday & Co., accepted the novel Carrie for publication, providing him the means to leave teaching and write full-time. He has since published over 50 books and has become one of the world's most successful writers. King is the recipient of the 2003 National Book Foundation Medal for Distinguished Contribution to the American Letters and the 2014 National Medal of Arts."),
]

class AuthorList(TemplateView):
    template_name = 'author_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Author.objects.all()
        return context