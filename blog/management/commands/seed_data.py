# blog/management/commands/seed_users_posts.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import transaction
from django.core.exceptions import FieldDoesNotExist

import sys

# Adjust this import if your Post model lives elsewhere
from blog.models import Post

User = get_user_model()
PASSWORD = "TestPass123"

# Users only contain username and email
users_data = [
    {"username": "femiadeniyi", "email": "femiadeniyi@yopmail.com"},
    {"username": "chukwumaokoro", "email": "chukwumaokoro@yopmail.com"},
    {"username": "aishamusa", "email": "aishamusa@yopmail.com"},
    {"username": "nnekaadedeji", "email": "nnekaadedeji@yopmail.com"},
]

# Full, un-truncated post contents exactly as provided
posts_by_user = {
    "femiadeniyi": [
        {
            "title": "Finding Quiet in the Middle of a Noisy City",
            "content": """
When I first moved from my hometown to Lagos I thought the biggest challenge would be the traffic. I did not expect to find myself learning how to reclaim quiet inside an otherwise loud life. The city is full of noise and motion, but it also taught me that stillness is a skill you can practice.

In the beginning I reacted to the noise. I rushed between errands, ate at my desk, and fell asleep with the television on because it felt strange to be in such vast silence. Then I noticed that some people brought small rituals into their days. An early morning jogger who always paused to stretch under the same mango tree. A market vendor who took ten deliberate minutes to sit and sip tea. These quieter choices looked intentional, and I started to try them for myself.

My first deliberate step was small and, honestly, almost silly: I took a route home that added an extra ten minutes of walking. The longer path had older trees and a narrow storefront that sold secondhand books. Walking slowly instead of rushing gave me time to notice the smell of grilled plantain rotating on a street cart and the way sunlight patterned through mango leaves. Those ten minutes started to anchor my evenings.

I also started scheduling nothing. Not because I had endless free time, but because even in the busiest week I could find fifteen minutes that I designated for nothing in particular. Sometimes that time was spent on breathing exercises that felt less like a task and more like resetting the day. Other times I simply sat on a small bench outside my building with a cup of tea and watched the world move around me. It turned out that nothing tasks had a shape: I showed up, I sat, and I let my pace slow down.

Rituals helped me notice the difference between silence and presence. Silence meant the absence of sound; presence meant attention. One evening I discovered a rooftop where neighbors gathered with simple snacks and soft conversation. It was not libraries-quiet, but there was an attentive sweetness to it. People were present with each other and with the moment, and the atmosphere was calm in a way that made me realize I had been chasing the wrong thing. I wanted presence more than silence.

I began to adapt daily chores into restful practice. Cooking became a focus exercise where chopping, stirring, and tasting anchored my mind. Washing dishes, long an afterthought, became a small ritual. The rhythmic motion and warm water reduced the mental noise that followed me from my phone. Small chores turned into opportunities for presence.

There were complications. Family obligations, work deadlines, and weekends that filled themselves quickly. Some days nothing helped. On those days I learned to be gentler with myself. I did not force calm; I accepted the messy energy and waited for the next small practice. What changed over months was my ability to return to quiet without guilt, so it did not have to be perfect to matter.

If you want to practice quiet, start with tiny choices. Take the longer walk, make a cup of tea without scrolling, tidy one corner of a room, or close your eyes for five minutes. The point is not to build a perfect life but to create spots of steadiness you can step into when the world gets loud. The city will still be noisy, but you will possess pockets that let you breathe, notice, and return refreshed.
"""
        },
        {
            "title": "Small Houses, Big Decisions: Living with Less",
            "content": """
When I moved into a smaller apartment to cut costs and be closer to work, I assumed I was trading space for convenience. The reality was more complex and, ultimately, more freeing. Shrinking my physical footprint forced me to make frequent decisions about what I valued and what I could let go of. It changed my relationship with stuff, time, and attention.

At first it was practical. I had to reconsider every piece of furniture and every utensil. I realized I had been holding on to possessions because they came with memories, or because I thought I might need them someday. That imaginary day rarely arrived. So I made a rule: if an item had not been used in a year and did not bring regular joy, it would be donated. The process felt ruthless at times, but it also felt clarifying.

The smaller space also altered how I entertained. Hosting full-house dinner parties became less frequent, but the gatherings I did have were more intimate and intentional. A small living room meant that when friends came over we were physically close, and the conversations seemed deeper for it. I learned to appreciate quality over quantity—one good conversation felt worth more than several shallow ones.

Storage decisions taught me about organization and ritual. I invested in a few thoughtfully chosen containers and learned to label boxes in plain language. This made daily life easier and cut down the stress of lost items. There was also a bonus effect: I started to buy less because I had fewer places to put things. Each purchase required a small conversation with myself: is this something I will use regularly? Does it deserve space in my life?

Living with less also made me rethink my relationship with experiences. I started to spend on small, meaningful activities—a pottery class, a short road trip, a well-made meal—rather than on things that would gather dust. The return on these experiences was immediate: memories, skills, and new social connections. The apartment became a place to recover from experiences rather than a place to store them.

Not everything about the transition was smooth. There were adjustments and moments of frustration. But over time the smaller space felt like an ally rather than a limit. It encouraged me to be selective, to value presence, and to treat everyday life with more intentionality. If you are considering a reduced living space, prepare to make many little decisions. Those decisions turn into a lifestyle that can be quieter, friendlier, and richer in ways that were not obvious at first.
"""
        },
        {
            "title": "A Year of Daily Walks and the Tiny Ways They Add Up",
            "content": """
I decided a year ago to walk every day, no matter how short the route. At the time it felt like a small challenge more about discipline than transformation. A year in, I would say the practice changed my perception of time, my social life, and even my appetite. It was not dramatic but cumulative, the kind of change that reveals itself in small increments.

My rule was simply this: walk for at least twenty minutes daily. Some days that meant a brisk route around the block. Other days a slow meander through a nearby market. The only non-negotiable was the time—twenty minutes of feet on pavement, being in motion without a specific destination. That constraint turned into a gift. The act of moving carried my thoughts to new places.

Walking became my thinking time. I started to use the time to work through problems that felt stuck at my desk. If I needed to make a decision, I walked. If I needed quiet reflection, I walked. The repetitive motion seemed to line up with my thought patterns in a productive way. I found it easier to see alternative angles on work issues and to feel less overwhelmed.

I also noticed the social side of walking. I met neighbors who also walked at odd hours and small friendships formed from shared sidewalks. A vendor I passed every morning became someone I would stop to chat with about the weather and the day's produce. These interactions were short but real. They added a texture to my days that felt grounded.

Physically, the habit improved my sleep and hunger rhythms. On days I walked, I slept better. On days I skipped, I noticed restlessness. Walking also improved my appetite patterns without making me obsess about calories. I simply felt more satisfied with meals and more inclined to prepare wholesome food.

There were hurdles—rainy seasons, busy schedules—but the simplicity of the rule kept me going. When weather or timing made twenty minutes difficult, I chopped the time into two shorter walks. The practice adapted to life rather than life adapting to it. That's the real lesson: sustainable habits are flexible.

If you are considering a similar habit, pick a simple rule and keep it manageable. Start small, stay consistent, and be willing to adapt. Over months, small choices add up to noticeable changes. Walking taught me that a daily practice need not be dramatic to be meaningful. It only needs to be honest and repeatable.
"""
        },
    ],
    "chukwumaokoro": [
        {
            "title": "Growing Up on Pepper Soup and Plantain: Food and Memory",
            "content": """
My earliest memories of food are noisy: the sound of cassava grating, the splash of palm oil in a frying pan, and the laughter of extended family around a low table. Food in my childhood was a social act that connected taste to place, and even now certain dishes—pepper soup, roasted plantain, jollof rice—transport me instantly back to those afternoons.

Pepper soup was a household ritual on busy days and evenings when someone returned tired from work. The soup is uncomplicated but precise: broth made fragrant with calabash nutmeg, a few grains of uziza, and soft chunks of meat that melt into the stock. There is an intimacy to spooning that soup while the rest of the house hums. These meals taught me that comfort often lives in simple, well-made food.

Plantain was another constant, whether ripe and caramelized or green and fried into dodo. I learned that the same ingredient can be transformed into different moods depending on preparation. A plate of warm, ripe plantain with a small pot of palm oil is celebratory in its sweetness. Fried green plantain with pepper and beans is pragmatic fuel for a long day. Food signaled both celebration and sustenance.

As I grew older and moved away from family, cooking became my way to maintain those connections. I started to recreate the flavors I missed, learning to measure with my senses rather than precise weights. I would crowd a small kitchen with friends and teach them how to knead fufu or toast spices until they smelled alive. The kitchen became both a classroom and a place for small parties.

Food also shaped my friendships. Hosting a meal felt like an effortless way to show care. I would invite one friend, then another, and soon there was a habit of gathering around a table to trade stories and share dishes. It did not have to be elaborate—sometimes a simple pot of steaming rice and beans shared with good conversation was enough.

Lately I find myself experimenting with hybrid recipes: pepper soup infused with lemon grass, plantains paired with spicy tomato stews, or grilled fish with a light chi-chi pepper sauce. These experiments are not attempts at authenticity but rather invitations to expand the flavors that shaped me. The result is food that honors memory while inviting innovation.

If you love food and want to connect more with your past, try cooking one memory meal a week. Invite someone, tell the story of the dish as it cooks, and let the act of sharing deepen both taste and relationship. Food is memory you can taste, and sharing it makes the memory richer.
"""
        },
        {
            "title": "Sunday Market Runs: Buying Well and Cooking Better",
            "content": """
Sunday market runs are a weekly ritual I rarely skip. They are part economics, part theater, and wholly sensory. I go for the best tomatoes, the freshest fish, and the occasional impulse vegetable that looks too interesting to leave. Markets are where I refine what I cook during the week.

My routine starts early. The best produce doesn't wait. I walk the aisles of the market with a canvas bag, evaluate the tomatoes by feel, and learn which vendor has the crispest okra that week. These small choices affect meals for the whole week. Picking an aromatic bunch of basil or a handful of fragrant uziza can change the character of a stew, and I have learned to trust my hands and nose when choosing ingredients.

Markets are also classrooms. I ask vendors about seasons and storage tips. Once I learned to ask how long a vegetable had been in stock, and that small piece of information changed how I planned meals. I began to cook with what was freshest instead of chasing exotic ingredients. That shift simplified shopping lists and made weeknight cooking less stressful.

There is also a social layer. Vendors remember faces and preferences. A fishmonger might set aside a small portion he knows I like, while a fruit seller will give a quick tip about ripeness. These interactions are transactional but also friendly, small anchors in my week that make grocery shopping feel like a practice rather than a chore.

Cooking from market purchases has made my meals more seasonal. Instead of forcing a recipe because I saw it online, I build menus around what is vibrant that day. This approach is both economical and more delicious. There is a distinct difference between a tomato that burst with sun in the field and one that traveled across multiple cities.

If you want to get more joy out of cooking, visit a market with curiosity. Buy thoughtfully, ask questions, and plan simple meals that highlight what you found. The payoff is in the taste and in the small conversations that stitch you to your local food system.
"""
        },
        {
            "title": "Learning to Cook Fish Without Fear",
            "content": """
For a long time I avoided cooking whole fish. The idea of cleaning, seasoning, and grilling felt like a complicated ritual I did not have the skill to perform. Then one weekend I decided to try, partly out of stubbornness and partly because I missed the smoky taste from street grills.

My first attempts were awkward: burnt edges, underseasoned flesh, and a pan that stuck. But I kept going. I learned basic prep: scaling or asking the vendor to clean the fish, scoring the sides to allow heat and flavors to penetrate, and basting with a light mixture of lime, ginger, and a little oil. Small techniques made large differences.

Grilling transformed the fish. A modest charcoal grill offered a smoky finish that a pan could not replicate. But even a heavy skillet can produce pleasant results if you preheat it properly and avoid moving the fish too soon. Let the skin crisp, then flip carefully and finish in the oven if needed. Patience helps.

Serving matters as much as cooking. A squeeze of citrus, a side of pepper sauce, and a simple salad turned humble fish into a memorable meal. I started to invite friends and share these dishes, and their reactions were encouraging. What felt once like an intimidating ritual became a shared pleasure.

If you are intimidated by whole-fish cooking, start small. Practice on a medium-size fish, ask your vendor to clean it, score the sides, and test a simple seasoning. Expect imperfections and treat them like experiments. Over time these attempts build confidence and reward you with tastes that feel more honest and satisfying than many takeout options.
"""
        },
    ],
    "aishamusa": [
        {
            "title": "Weekend Road Trip: Discovering a Quiet Town Near the City",
            "content": """
I did not plan to find a town that felt like a secret. The weekend started as a simple escape: I wanted slower streets, local market colors, and a different sky. Two hours by road I found a place with narrow lanes, a small river, and a bakery that filled the morning with yeast and sugar.

Driving there felt like moving through eras. As the city thinned, roadside stands gave way to clusters of houses, and fields opened up. I stopped at a roadside stall for fresh coconut water and a chat. The vendor recommended a small guesthouse by the river and a family-run cafe that served pastries made with local butter. The spontaneity of those recommendations made the trip feel like an authentic discovery rather than a tourist checklist.

The town's market was the heart of the visit. People traded vegetables and stories and there were old men playing chess with a seriousness that made me slow down. I ordered a plate of local stew and a soft roll in the cafe. The stew felt like flavor grown from the soil around the town; it had a steadiness and depth that reminded me food is often best where it is produced.

I rented a small room with a balcony that faced the river. In the late afternoon I walked across a footbridge and watched children race each other from a low bank. The pace there made me rethink what I value in a trip. Instead of trying to cram every sight into my itinerary, I allowed space for unscheduled hours and found beauty in small routines: a second cup of coffee, a long conversation with a baker, and an early evening stroll.

The trip reminded me that travel can be a practice of slowing down. You do not always need to cross oceans to see new patterns. Sometimes a short drive and a willingness to follow local tips are enough to reset perspective and return home with a small stack of new memories and a few recipes scribbled on a napkin.
"""
        },
        {
            "title": "Solo Travel Lessons: How I Learned to Trust My Instincts",
            "content": """
I started traveling alone because friends' schedules never matched mine. That necessity turned into a habit that changed how I navigate new places and people. Solo travel taught me to trust my instincts, to plan modestly, and to be comfortable with quiet evenings that are mine alone.

Early solo trips were clumsy. I would overpack out of a fear of being unprepared. I would avoid small talk, thinking I was more vulnerable alone. Over time I corrected each tendency. I learned to pack light and to approach strangers with curiosity rather than suspicion. In hostels and guesthouses I practiced short, honest conversations that opened up routes I would not have discovered on my own.

Trust is the core lesson. When something feels off, I leave. When a local offers a tip that feels right, I try it. That balance between caution and openness is practical and freeing. It prevents paranoia and invites serendipity. I discovered that people are often more helpful than my worst anxieties predicted.

Solo travel also improved my planning skills. I started to book accommodation with a small checklist: safety, reviews from other solo travelers, and proximity to the town center. I made contingency plans for transport and always kept a local SIM card for navigation. These practical steps increased confidence and made the actual travel more enjoyable.

Being alone on the road gave me a unique kind of adulthood. I learned to pace myself, to choose meals for one with more pleasure, and to enjoy evenings of reading or journaling with a soft soundtrack. Those slow nights became part of the trip's richness rather than an absence.

If you want to travel solo, start with a short trip close to home. Build small wins and learn your comfort zones. Solo travel will not fix everything, but it will give you practice in trust, planning, and delightful solitude.
"""
        },
        {
            "title": "Packing Light: What I Bring on a Three-Day Getaway",
            "content": """
Over lots of short trips I developed a minimalist packing strategy that makes three-day getaways feel breezy. My goals are simple: be comfortable, stay flexible, and carry only what I will likely use. The result is less luggage and more freedom during the trip.

First, I pick a compact bag that I can carry comfortably. A small duffel or carry-on backpack keeps me mobile. Next, clothes: two tops, one pair of trousers, a light sweater, and a versatile dress or shirt if I expect something more formal. I always include a pair of comfortable walking shoes and a lighter pair for evenings if needed.

Toiletries are in travel-sized containers and I keep a small first-aid kit. Electronics are minimal: phone, charger, and a lightweight power bank. If I plan to work a little, I bring a small tablet rather than a laptop. A reusable water bottle and a foldable tote are useful for markets and unexpected purchases.

I also pack a small notebook and a pen. It sounds quaint, but writing even a line about the day helps the trip settle into memory. I rarely overpack clothing because I prefer shopping locally if I need something. This practice reduces the guilt of buying a small item and makes travel more fun.

The advantage of packing light is both practical and mental. Less luggage means less worry about lost bags and more opportunity for spontaneous detours. If you are trying to travel more, shorten your packing list and see how much more flexible you feel.
"""
        },
    ],
    "nnekaadedeji": [
        {
            "title": "How I Started Using AI Tools to Speed Up Small Tasks",
            "content": """
I was skeptical about AI tools for a while. Some of the examples online felt flashy and out of reach for daily use. Then I tried one simple tool to summarize long articles, and it changed my workflow. Small automation built around real tasks started saving me time in ways that felt practical rather than futuristic.

I use AI in a few modest ways. For example, I feed meeting notes into a summarizer to extract action items. The results are not perfect, but they are often accurate enough that editing is faster than transcribing everything manually. Another small use is drafting email replies. I provide context and a desired tone, and the generated draft gives me a solid starting point that I customize. This is not cheating; it is a way to move faster while staying human.

Using AI responsibly is important to me. I always check facts and never allow a tool to send something without review. I also pay attention to privacy. I avoid uploading sensitive personal or company data to third-party tools. These guardrails keep AI useful without becoming a source of risk.

An unexpected benefit has been skill development. By using AI to prototype small ideas, I can iterate faster. For example, when I sketch an app feature, I use a tool to create sample user flows and then refine the output. This process allows me to test concepts quickly before investing time in code.

The emotional effect is interesting too. Some tools make routine tasks feel lighter, reducing mental friction. That frees time for creative work: thinking about product direction, designing interactions, or learning new technologies. The automation of small tasks amplifies the work humans do best.

If you want to try AI for productivity, start small. Identify a repetitive task you do often, pick a trustworthy tool, and use it to prototype an improved workflow. Always add human review and be mindful of privacy. Small, sensible uses can add up to meaningful gains in time and clarity.
"""
        },
        {
            "title": "Building Tiny Automations That Actually Help",
            "content": """
Automation does not have to be a massive engineering project. Some of the most helpful automations I've built were small scripts that solved a single annoying task. The trick is to focus on pain points that are frequent but low complexity.

One example is a small script I wrote to rename and organize downloaded files. It watches a downloads folder and moves files into dated folders with standardized names. The script is less than a few dozen lines and saved me from hours of manual sorting. Another is a short personal script that pulls my calendar events and generates a simple daily checklist. It keeps my day focused without heavy overhead.

When building automations, it helps to keep them visible. If an automation runs entirely in the background with no feedback, it can develop bugs unnoticed. I prefer automations that produce a short summary or an email so I can confirm they ran correctly. That small transparency prevents surprises.

Automation also changed my approach to learning. Instead of trying to learn a new technology end-to-end, I learned just enough to build a micro-solution. These micro-projects provide immediate value, which motivates me to learn more deliberately.

If you want to start with automation, identify a repetitive task you do daily and write a small script or use a no-code tool to handle it. The satisfaction of removing an annoyance is immediate, and the time saved compounds quickly.
"""
        },
        {
            "title": "Ethics and Small-Scale AI: What Developers Should Think About",
            "content": """
Most conversations about AI ethics focus on large-scale harms, but as a developer I think it is equally important to consider small-scale impacts. Even modest tools can introduce bias or privacy issues if we are not careful. When designing utilities that will touch users' data, I ask three simple questions: who benefits, who might be harmed, and how is data stored?

I start every small project with guarded inputs. If my tool uses user data, I minimize what I collect and keep it local when possible. For teams, having a short ethics checklist before shipping a feature helps us consider consequences we might otherwise skip. It can be as simple as asking whether the tool could leak information, unfairly penalize a user, or misrepresent facts.

Transparency matters. When a tool uses automated decisions, I try to explain how it works in plain language. That helps users correct mistakes and provides context for trust. I also include a quick path to human review because automation should augment human judgement, not replace it.

Finally, I keep the feedback loop short. When users report problems, I prioritize fixes that reduce harm quickly, even if they are not perfect. These small ethical practices make building AI tools responsibly feasible for small teams or solo developers.

If you are building with AI, keep ethics local: address the small harms that are likely to happen today, not only the large hypothetical risks. Practical, immediate ethics reduces friction for users and helps make the technology safer for everyone.
"""
        },
    ],
}

def detect_author_field():
    for candidate in ("author", "user"):
        try:
            Post._meta.get_field(candidate)
            return candidate
        except FieldDoesNotExist:
            continue
    return None

@transaction.atomic
def seed():
    created_users = []
    for u in users_data:
        username = u["username"]
        email = u["email"]

        user, created = User.objects.get_or_create(username=username, defaults={"email": email})
        if created:
            user.set_password(PASSWORD)
            user.save()
            print(f"Created user: {username} ({email})")
        else:
            user.email = email
            user.set_password(PASSWORD)
            user.save()
            print(f"Updated existing user: {username}")

        created_users.append(user)

    total_created = 0
    author_field = detect_author_field()

    for user in created_users:
        posts = posts_by_user.get(user.username, [])
        for p in posts:
            title = p["title"]
            content = p["content"].strip()
            # ensure no literal double-dash sequences
            content = content.replace("--", "—")

            create_kwargs = {"title": title, "content": content}
            if author_field:
                create_kwargs[author_field] = user

            try:
                post = Post.objects.create(**create_kwargs)
            except TypeError:
                # fallback: create minimal, then attach author if possible
                post = Post(title=title, content=content)
                try:
                    post.save()
                except Exception as e:
                    raise RuntimeError(f"Failed to save Post(title={title!r}). Check required fields. Original error: {e}") from e
            except Exception as e:
                raise RuntimeError(f"Failed to create Post(title={title!r}) with kwargs={create_kwargs}. Error: {e}") from e

            # If the model didn't allow author in create kwargs, attach now if possible
            if not author_field:
                if hasattr(post, "author"):
                    try:
                        post.author = user
                        if hasattr(post, "date_posted"):
                            setattr(post, "date_posted", timezone.now())
                        post.save()
                    except Exception as e:
                        print(f"Warning: could not set author on post '{title}': {e}", file=sys.stderr)
                elif hasattr(post, "user"):
                    try:
                        post.user = user
                        if hasattr(post, "date_posted"):
                            setattr(post, "date_posted", timezone.now())
                        post.save()
                    except Exception as e:
                        print(f"Warning: could not set user on post '{title}': {e}", file=sys.stderr)

            total_created += 1
            print(f"Created post '{title}' for {user.username}")

    print(f"Seeding complete. Created/updated {len(created_users)} users and {total_created} posts.")

class Command(BaseCommand):
    help = "Seed 4 users and create conversational blog posts for each."

    def handle(self, *args, **options):
        self.stdout.write("Starting seed process...")
        seed()
        self.stdout.write(self.style.SUCCESS("Seeding finished."))
