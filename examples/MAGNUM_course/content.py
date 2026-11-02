# Ultimate YouTube Client Acquisition And Branding Course. Build: python3 tools/docbuilder_v3.py content.py "<title>.docx" --img-dir img
P = os.path.dirname(os.path.abspath(__file__)) + '/' if '__file__' in dir() else './'
title_page('The Ultimate YouTube Client Acquisition And Branding Course',
           [('The ', False), ('Full', True), (' System, Step By Step', False)], hero='hero_v3.jpg')
toc_page(levels=1)

h1('Who This Is For')
para('Coaches, consultants and service businesses doing about $50,000 to $100,000+ a month whose channel is inconsistent, gets no views, or gets views but no buyers.')
para("This is not for beginners or AdSense chasers. Everything in here is measured in calls booked and clients closed.")
flow([('Phase 0', 'The Market'), ('Phase 1', 'Ideas'), ('Phase 2', 'Systems'), ('Phase 3', 'Execution'), ('Phase 4', 'Maintenance')])

h1('Who We Are')
para("My name is Bryan, and I run Viral Bangers with my co-founder Mauricio. We're a YouTube agency for business owners who sell something. We handle the ideas, the scripts, the editing and the thumbnails, so all you have to do is show up and record.")
para("We've generated over $10 million from YouTube for 100+ clients, written over a thousand scripts, and one of my own videos made $275,766. One of the creators we work with is Brad Goh (The Trading Geek), who has over 1.8 million subscribers.")
bullets(["Chamath Palihapitiya: we edit all of his long-form videos.",
         "Brad Goh (The Trading Geek): we work with Brad on his YouTube channel, which has over 1.8 million subscribers.",
         "Jordan Welch: we scripted \"getting rich is easy, actually\", which has 923,571 views.",
         "Inayah McMillan: our very first video together did 1,185,797 views.",
         "Ethan Garland: we worked on two of his top three videos, including one with 539,000 views.",
         "Scott Taylor: his views went from about 3,600 a video to 15,000, and YouTube now brings in around $40,000 a month.",
         "Fiction Profits Academy: 7,000 to 15,000 subscribers, and they're the top result for \"how to start a KDP business\".",
         "Clover Trading: average views went from about 1,000 a video to 8,000."])
img('clients.jpg', 6.5)
img('logos.jpg', 6.5)

for n in range(5):
    exec(open(P + f'phase{n}.py').read())

h1('The Checklist')
checklist(['Decide the game: you play for buyers and booked calls',
           'Write down your buyer, your unfair advantage, your proof and your message',
           'Pick one thing to be known for and keep the look consistent',
           'Research demand vs supply before you write a single idea',
           'Generate ideas in bulk, score them, kill most of them before filming',
           'Title and thumbnail first, script second',
           'Script for aha density, with a hook that states proof, desire and value',
           'Every video has one CTA and a funnel behind it, with tracking from video to booked call',
           'At least 2 editors and written SOPs before you scale uploads',
           'Record with camera, light and mic sorted, then hand off the edit',
           'Repurpose each long video into short clips',
           'Read analytics from the money backwards and fix the lowest broken step',
           'Keep a test slot for new formats so the channel never goes stale',
           'Run the first 90 days and judge it on calls per video'])

h1('Want Us To Do This For You?')
para('We build and run this whole system for you: ideas, scripts, editing, thumbnails, funnels and tracking. You show up and record.')
para('**Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]')
