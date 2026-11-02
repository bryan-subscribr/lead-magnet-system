# LM1 SCOTT: the Scott Taylor case study (v1, 2026-10-06).
# Build: python3 ~/.claude/skills/lead-magnet-doc/scripts/docbuilder.py content.py "Scott Taylor Case Study.docx" --img-dir img
title_page('Case Study: How Scott Taylor Went From A Dead Channel To Making $40,000 A Month',
           [('And ', False), ('Exactly', True), (' How To Build Yours', False)], hero='hero.jpg')
toc_page()

# ================= TL;DR =================
h1('TL;DR')
para("When Scott Taylor came to us, he was convinced YouTube had restricted his channel. His videos used to get 14,000, 20,000, even 30,000 views. Then everything dropped to around 5,000, and most of his clients were coming from ads.")
para("The channel wasn't restricted. The videos just weren't doing the right jobs, and nobody could tell which ones were actually bringing in money.")
para("So we changed three things:")
bullets(["We tracked every booked call back to the video it came from.",
         "We gave every video one of two jobs: bring new people in, or turn them into booked calls.",
         "We made sure every video sent people to one clear next step."], numbered=True)
para("His views went from about **3,600 a video to 15,000.** One video got **37,343 views and booked around 10 qualified calls.** And YouTube now brings in **around $40,000 a month on average.**")
para("A few words I'll use a lot in this doc, so you know what I mean:")
bullets(["Reach video: a video made to bring new people to your channel. Broad topic, lots of people care about it.",
         "Targeted video: a video made for someone who is already close to buying. Fewer people click, but the right ones do.",
         "Funnel: wherever the video sends people next. A call link, a free guide, an application form.",
         "Qualified call: a booked call with someone who could actually afford to buy."])
para("In this doc I'll show you what Scott's channel looked like before, every video we made, what worked, what didn't, and then how to plan your own next 6 videos. You don't need to be a trader, and you don't need 35,000 subscribers.")

# ================= WHO WE ARE =================
h1('Who We Are')
para("My name is Bryan, and I run Viral Bangers. We're a YouTube agency for business owners who sell something, like coaches, traders, consultants and info product businesses. We handle the ideas, the scripts, the editing and the thumbnails, so all you have to do is show up and record.")
para("A few of the people we've worked with:")
bullets(["Chamath Palihapitiya: we edit all of his long-form videos.",
         "Jordan Welch: we scripted \"getting rich is easy, actually\", which has 923,571 views.",
         "Inayah McMillan: our very first video together did 1,185,797 views.",
         "Ethan Garland: we worked on two of his top three videos, including one with 539,000 views.",
         "RP Profits: 8,000 to 47,900 subscribers with one thumbnail he uses on almost every video.",
         "Fiction Profits Academy: 7,000 to 15,000 subscribers, and they're the top result for \"how to start a KDP business\".",
         "Clover Trading: average views went from about 1,000 a video to 8,000."])
img('clients.jpg', 6.5)
img('clients2.jpg', 6.5)
para("Scott Taylor is one of those clients too, and his story is the one I get asked about the most.")

# ================= WHO =================
h1('Who Is Scott Taylor?')
para("Scott Taylor (**@scotttaylorfx**) is a forex and futures trader. He runs Evolution Markets FX and sells 1-1 coaching. Right now his channel has about 35,700 subscribers.")
img('thumb_bpCrCbBbV4M.jpg', 5.0)
para("Now, you might be thinking: \"Bryan, I'm not a trader, and I don't have 35,000 subscribers. Why should I care?\"")
para("Because this isn't really a trading story. It's the story of a business that sells something, using YouTube to get booked calls instead of chasing views. And the part that fixed his channel had nothing to do with how many subscribers he had. It was about knowing what each video is for.")
para("I'll show you how to do the same thing for your business later in this doc.")

# ================= BEFORE =================
h1('Before Working With Us, He Thought His Channel Was Dead')
para("Back in late 2025, Scott's videos were doing well. 14,000 views, 20,000, even 30,000 on a good week.")
img('before_2025.jpg', 6.0, caption='(Two of his videos from before the drop.)')
para("Then it fell off a cliff. Videos that used to get 15,000 views started getting 5,000.")
img('channel_year.jpg', 6.5, caption='(His channel over the last 365 days. You can see the drop at the start of 2026.)')
para("When that happens, almost everyone blames the algorithm. Scott was sure his channel had been restricted. And I get it. It feels like somebody switched something off.")
para("But I've looked at a lot of channels like this, and the answer is almost never \"YouTube hates you\". It's usually two things:")
bullets(["Every video is trying to do the same job.",
         "Nobody knows which videos actually make money."], numbered=True)
para("Scott had both. Most of his clients were coming from ads, so YouTube had turned into something he did on the side, without really knowing what it was doing for the business.")
para("**Try this:** write down your last 10 videos. Next to each one, write how many clients it brought in. If you can't fill in that column, that's the first thing to fix, and it's exactly where we started with Scott.")

# ================= TRACKING =================
h1('First, We Tracked Which Videos Booked Calls')
para("Before we changed a single video, we set up tracking, so every booked call could be traced back to the video it came from.")
para("This sounds boring. It's the most important thing in this whole doc.")
para("If you don't track, you end up judging your videos by views. And views will lie to you. A video with 40,000 views can book zero calls, and a video with 3,000 views can book five. If you can't see that, you'll keep making more of the wrong ones.")
para("For Scott we used the call-tracking system we run for all our clients. It shows every booking and which video sent it.")
img('tracio_chart.jpg', 6.5, caption='(Bookings from YouTube, day by day, once tracking was switched on.)')
para("You don't need a tool like that to start. The free version looks like this:")
bullets(["Make one link per video. Any free link shortener works, or add something like ?src=video12 to the end of your booking link.",
         "Put that link in the first line of the description and in a pinned comment.",
         "Add one question to your booking form: \"Which video sent you here?\""], numbered=True)
para("That's it. After a few weeks, you'll know which videos bring in calls, and which ones just bring in views.")
para("**Try this:** add that one question to your booking form today. It takes two minutes.")

# ================= TARGETED =================
h1('His Targeted Videos Booked Calls, But Not Enough People Found Him')
para("We started with targeted videos. Deep, technical videos for someone who already trades and is thinking about getting coaching.")
img('targeted_trio.jpg', 6.5)
para("\"Watch Me LIVE Backtest My Science-Backed Scalping Strategy\" (that's him testing his strategy on old charts, live), \"We Tested 1,000 Trading Strategies, So You Don't Have To\" and \"10 Years Of Trading Experience In 33 Minutes\".")
para("They got **3,212 to 4,048 views each.** Not exactly exciting. But between them, they booked **around 7 calls.**")
para("That's roughly one booked call for every 1,500 views. For a business, that's really good. These videos did their job, which was to turn the people already watching into calls.")
para("The problem was that not enough new people were finding him. Targeted videos are great at converting a small group of warm viewers, but they don't grow that group. If you only make targeted videos, you end up selling to the same few thousand people over and over again.")
para("**Try this:** write down the 3 questions people ask you most on sales calls. Each one is a targeted video.")

# ================= REACH =================
h1('Then We Added Videos That Bring New People In')
para("So we changed the strategy. We started making reach videos: broad topics that anyone in his market would click on. But every one of them still pointed to the same next step, a booked call with Scott.")
para("The first two did almost 9,000 views each:")
img('reach_pair.jpg', 6.5)
para("Scott noticed straight away:")
img('wa_top_content.jpg', 3.5, caption='("Nice, yes videos getting more eyes now I like to see it")')
para("Then we put out \"I Finally Revealed My Most Effective Scalping Strategy (For Free)\".")
img('big_video.jpg', 6.5)
para("**37,343 views.** His biggest video in over a year, and YouTube told him it was doing 9.7 times better than usual. More importantly, it booked **around 10 qualified calls.**")
para("This is the one that made it click for him:")
img('wa_double_down.jpg', 3.5, caption='("Definitely found what we need to double down on")')
para("Notice what we said back in that chat: it got traction mainly with new audiences. That's the whole point of a reach video. And beginner guides tend to have a bigger market, because there are always more beginners than experts.")
para("Now, you might be thinking: \"Bryan, but the targeted videos booked more calls per view.\"")
para("You're right. The 37,000-view video booked roughly one call for every 3,700 views, which is less efficient than the targeted ones. But it brought in way more people in total, and every one of those people is now a viewer who can watch the targeted videos next. You need both. Reach videos fill the pool, and targeted videos turn the pool into calls.")
para("**Try this:** take one of your targeted ideas and make it broader. Keep the promise, but widen who it's for. \"How I help SaaS founders cut churn\" becomes \"Why most businesses lose customers (and the fix)\".")
h2("You Don't Need A Big Edit")
para("One more thing from this phase. Scott's latest video at the time, \"If You Understand Math, You Understand Trading\", is completely raw. It's just him drawing on an iPad, with no fancy editing.")
img('math_video.jpg', 6.5)
para("It got **17,000 views in 5 days and booked 3 calls.** It was a really good format for reaching new people, and they loved it.")
img('wa_math_update.jpg', 3.5, caption='(Our weekly update to Scott\'s team.)')
para("So if editing is the thing stopping you from posting, it shouldn't be. The idea and the packaging (the title and the thumbnail) do most of the work.")

# ================= RESULTS =================
h1('Did It Work? Here Are The Numbers')
para("Every long-form video we made together, July to September 2026:")
img('all_videos.jpg', 6.5)
table([['Video', 'Job', 'Views'],
       ['Watch Me LIVE Backtest My Science-Backed Scalping Strategy', 'Targeted', '4,048'],
       ["We Tested 1,000 Trading Strategies, So You Don't Have To", 'Targeted', '3,212'],
       ['10 Years Of Trading Experience In 33 Minutes', 'Targeted', '3,553'],
       ['How To Get Funded SO FAST It Feels Illegal', 'Reach', '8,918'],
       ["Liquidity + Timing = The Perfect Entry (You're Missing This)", 'Reach', '8,611'],
       ['I Finally Revealed My Most Effective Scalping Strategy (For Free)', 'Reach', '37,343'],
       ["If I Started Trading Again In 2026, This Is Exactly What I'd Do", 'Webinar', '7,971'],
       ['The ONLY Trading Indicator You Need', 'Reach', '10,042'],
       ['If You Understand Math, You Understand Trading', 'Reach', '17,383']],
      [4.3, 1.1, 1.1])
para("(Views as of 29 September 2026.)")
para("The first three videos averaged about **3,600 views.** The six after we changed the strategy averaged about **15,000.** That's about 4x, and right back where the channel was at its best in 2025.")
para("And YouTube has been bringing in **around $40,000 a month on average.**")
h2('One Video, 200 Sign-Ups In 72 Hours')
para("Partway through, Scott switched to a webinar funnel, which means a free live training that people sign up for. We made one last-minute video for it, \"If I Started Trading Again In 2026\".")
img('webinar_video.jpg', 6.5)
para("It brought in **about 200 sign-ups in 72 hours.** From one video, made at the last minute.")
h2("What We're Not Claiming")
para("I want to be straight with you, because this part is just as useful as the wins.")
para("The webinar didn't convert great. Here's how it actually went:")
img('webinar_funnel.jpg', 3.5)
para("The video did its job. 200 people signed up. But only 1 of them paid. That's an offer problem, not a YouTube problem.")
para("Scott also switched offers a bunch of times during these three months. Every time the offer changed, the funnel basically started from zero again. With one steady offer, every number in this doc would be higher.")
para("He was also still running ads the whole time, and I'm not going to show his coaching price, so I won't pretend I can tell you exactly how many clients that $40,000 is.")
para("If you take one thing from this section, make it this: **pick one offer and leave it alone for 90 days.** YouTube can bring you the right people. It can't fix an offer that keeps changing.")

# ================= YOUR BUSINESS =================
h1("Make It Work For Your Business (You Don't Need To Be A Trader)")
para("Scott's market is huge. There are always more beginner traders. If you're a bookkeeper or a B2B consultant, your market is a lot smaller, and that's fine. You just need fewer, better calls.")
para("Here's what reach and targeted videos could look like in a few different businesses:")
table([['If you sell...', 'A reach video', 'A targeted video'],
       ['Sales consulting', 'Why most sales calls fail in the first 2 minutes', 'My exact discovery call script, line by line'],
       ['A marketing agency', 'How small businesses waste half their ad budget', 'We audited a $20,000/month ad account, live'],
       ['Bookkeeping or accounting', '5 money mistakes that kill small businesses', 'How I clean up 12 months of messy books'],
       ['Business coaching', 'Why most businesses stay stuck at the same revenue', 'Watch me fix a client\'s offer on a real call'],
       ['Software (SaaS)', 'The real reason customers cancel', 'How we set up onboarding for a 50-person team']],
      [1.6, 2.5, 2.4])
para("And you don't need a webinar. For most service businesses, the simplest funnel is the best one:")
para("**Video, then a booked call.** One link, at the top of the description and in the pinned comment, and one line at the end of the video telling people to click it.")
para("At your size, a reach video might get 500 views, not 37,000. That's okay. If that video books one call with a business that can pay you $5,000, it did more for you than a video with 50,000 views and no calls. Judge your videos by calls, not views.")

# ================= PLAN =================
h1('How To Plan Your Next 6 Videos')
para("Plan your next 6 videos before you write a single script. Fill in one row per video.")
table([['#', 'Working title', 'Job (reach or targeted)', 'Who it\'s for', 'Where it sends them', 'How you\'ll track it'],
       ['1', '', '', '', '', ''], ['2', '', '', '', '', ''], ['3', '', '', '', '', ''],
       ['4', '', '', '', '', ''], ['5', '', '', '', '', ''], ['6', '', '', '', '', '']],
      [0.3, 1.5, 1.1, 1.1, 1.3, 1.2])
h2('How To Fill It In')
bullets(["Start with your offer. Write down the one thing you sell. If you can't pick one, stop and pick one first. That's Scott's lesson.",
         "Write 3 reach ideas. Broad topics your whole market cares about. Ask yourself: would someone who has never heard of me click this?",
         "Write 3 targeted ideas. Use the questions people ask you on sales calls. Ask yourself: would a future client watch all of this?",
         "Give every video one next step. One link and one ask. If you give people three options, they pick none.",
         "Decide how you'll track it before you publish. One link per video, plus the \"Which video sent you here?\" question.",
         "Post them, then review after all 6 are out."], numbered=True)
h2('What To Say At The End Of Each Video')
para("For a reach video, keep it light. Most of these people just met you:")
para("*\"If you want help with this for your business, the link to book a call with me is at the top of the description.\"*")
para("For a targeted video, be direct. These people are close to buying:")
para("*\"If you want me to do this with you, book a call using the first link in the description. I'll look at your situation and tell you exactly what I'd do.\"*")

# ================= WORKING =================
h1("How To Tell If It's Working")
para("Commit to 6 videos, posting once a week. Don't judge anything until all 6 are out. Scott's channel didn't turn around on the first upload, it turned around once reach videos joined the mix.")
para("Then look at two numbers for each video:")
bullets(["How many calls did it book?",
         "How many new viewers did it bring in? You'll find this in YouTube Studio under Analytics, then Audience."], numbered=True)
para("Targeted videos should win on calls. Reach videos should win on new viewers. If a reach video brings in new people but books nothing, that's fine, it's doing its job. If a targeted video gets views but books nothing, look at the next step you're giving people, or look at your offer.")
para("Then make more of whatever is working. That's exactly what Scott meant when he said he'd found what to double down on.")

# ================= CHECKLIST =================
h1('Your Checklist')
para("Run every video through this before you hit publish:")
checklist(["I know if this is a reach video or a targeted video",
           "I know exactly who it's for",
           "It sends people to one next step, and only one",
           "That link is in the first line of the description and in a pinned comment",
           "The link is tracked, so I'll know if it books a call",
           "My booking form asks \"Which video sent you here?\"",
           "I'm selling the same offer I was selling last week"])

# ================= CTA =================
h1('Want Us To Do This For You?')
para("This is what we do at Viral Bangers. We set up the tracking, plan the reach and targeted videos, write the scripts and handle the editing, so all you do is record.")
cta_link('viralbangers.com', 'https://viralbangers.com')
