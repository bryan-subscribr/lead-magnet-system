# LM8 IDEAS: banger video ideas lead magnet, v1 (2026-10-06).
# Build: python3 ~/.claude/skills/lead-magnet-doc/scripts/docbuilder.py content.py "How To Come Up With BANGER Video Ideas.docx" --img-dir img
title_page('How To Come Up With BANGER Video Ideas That Build Your Brand And Get You Sales',
           [('And ', False), ('Exactly', True), (' Where To Find Topics And Formats That Already Work', False)], hero='hero.jpg')
toc_page(levels=1)

# ================= TL;DR =================
h1('TL;DR')
para("Most business owners spend 5 seconds on the idea and 5 hours on the edit. I'd flip that. If the idea is weak, nothing you do in editing will save the video.")
para("This doc is the exact process we use at Viral Bangers to come up with ideas for our clients. It's how we got Inayah McMillan **1,203,773 views** on the first video we ever made with her.")
para("Every banger idea has two parts:")
bullets(['a topic people already care about, which is what the video is about', "a format that's already worked, which is the shape of the title and the video"])
para("Then you add the one thing that makes it yours, which is your **unique advantage**: something true about you that a competitor can't say.")
para("Below you'll find where to find proven topics, 10 formats that worked for our clients, how to find your unique advantage, how to mix them into 25 ideas in 10 minutes, and how to score each idea before you film it.")
h2('If You Only Do Three Things')
bullets(['Write down 5 problems your buyers ask you about on sales calls. Those are your topics.',
         'Pick 3 formats from the list in this doc.',
         'Put them in the grid in Step 4, then add your unique advantage to the best 3 titles.'], numbered=True)
para("That's your next month of videos. Everything else in here makes those ideas better.")

# ================= WHO WE ARE =================
h1('Who We Are')
para("My name is Bryan, and I run Viral Bangers. We're a YouTube agency for business owners who sell something, like consultants, coaches, traders and info product businesses. We come up with the ideas, write the scripts, and handle the editing and thumbnails, so all our clients do is approve the ideas and hit record.")
para("Here are a few of the people we've worked with:")
bullets(["Inayah McMillan: the first video we made together has 1,203,773 views.",
         "Jordan Welch: we scripted \"getting rich is easy, actually\", which has 923,776 views.",
         "Ethan Garland: we worked on two of his top three videos, including one with 539,372 views.",
         "Scott Taylor: his views went from about 3,600 a video to 15,000, and YouTube now brings in around $40,000 a month.",
         "Fiction Profits Academy: 7,000 to 15,000 subscribers, and they're the top result for \"how to start a KDP business\".",
         "Clover Trading: average views went from about 1,000 a video to 8,000.",
         "Chamath Palihapitiya: we edit all of his long-form videos."])
img('clients.jpg', 6.5)
img('clients2.jpg', 6.5)
para("Every example in this doc comes from one of these channels or from my own.")

# ================= WHAT AN IDEA IS =================
h1('What A Video Idea Actually Is')
para("When most people say they have a video idea, what they actually have is a topic, like \"I should do a video on cold calling.\" That's only half an idea.")
para("A full idea is a **topic** plus a **format**.")
bullets(['The topic is what the video is about. Cash flow, cold calling, hiring your first salesperson, pricing, money mindset.',
         'The format is the shape of the title with the topic taken out. \"How I Brainwashed Myself to ___\" is a format. \"If I Started ___ Again In 2027\" is a format. You can drop almost any topic into the blank.'])
para("Then there's the third piece, which is what turns a good idea into a banger. Your **unique advantage** is something true about you that your competitors can't copy, like a result, a number, an age, a timeline or a story.")
para("Here's how that looked for Inayah. She teaches people how to start an Airbnb business, which is one of the most crowded niches on YouTube.")
table([['Part', "Inayah's video"],
       ['Topic', 'Money mindset (how you think about money)'],
       ['Format', '"How I Brainwashed Myself to ___", borrowed from two of Leila Hormozi\'s best videos'],
       ['Unique advantage', 'She became a millionaire at 20'],
       ['Final title', 'How I Brainwashed Myself to Be a Millionaire at 20']], [1.8, 4.7])
img('format_trio.jpg', 6.5, caption="(Leila's two videos on the left, ours on the right.)")
para("Each part does a different job. The topic decides who's interested. The format decides whether they click. The advantage is the reason they pick you over the hundred other people making the same video.")
para("If you leave one out, the idea gets weaker:")
bullets(['A topic with no format is a lecture. \"Cold calling tips\" could be anyone\'s video.',
         'A format with no advantage is a copy. \"How I Brainwashed Myself to Be Rich\" is just Leila\'s video again.',
         'An advantage with no topic people care about is a story nobody searches for.'])
para("So the process is in that order. Find a topic, find a format, add your advantage, then score it.")

# ================= STEP 1 TOPICS =================
h1('Step 1: Find A Topic People Already Care About')
para("You don't need to guess what your buyers want to watch. They've already told you, in three places.")
h2('Where To Find Proven Topics')
para("**1. Your sales calls.** Write down every question a prospect asks you before they buy. Every one of those is a video, and you already know the answer, because people pay you for it. This is the most underrated source of ideas I know, because it's free and nobody else has your calls.")
para("**2. The Popular tab of your niche.** Find 5 channels in your space. On each channel, tap Videos, then Popular. Write down the *topic* of their top 10 videos, not the title. If the same topic shows up in the top 10 of 3 or more channels, it's proven.")
para("**3. The comments under your competitors' best videos.** Look for questions and complaints that keep coming up. \"But what if my clients pay late?\" is a topic. So is \"this doesn't work for small teams\".")
para("You can also type your buyer's problem into the YouTube search bar and look at the suggestions that drop down. Those are things people are typing in right now.")
h2('What Topics Look Like For A Business')
para("Here's what that list might look like for two different businesses:")
table([['A sales consultant', 'A fractional CFO'],
       ['Cold calling', 'Cash flow'],
       ['Following up without being annoying', 'Pricing and margins'],
       ['Hiring your first salesperson', 'Paying yourself as the owner'],
       ['Handling "it\'s too expensive"', 'Taxes for small businesses'],
       ['Building a sales script', 'When to hire your first employee'],
       ['Using AI to book meetings', 'Using AI to run your finances']], [3.25, 3.25])
h2('Go One Step Wider Than Your Offer')
para("This is the part most people get wrong. They only make videos about the exact thing they sell, and those videos hit a ceiling fast, because only people who are already shopping will click.")
para("I think about topics in three rings:")
bullets(['Your offer, which is the exact thing you sell. A CFO\'s version is \"how to build a 13-week cash flow forecast\".',
         'Your buyer\'s world, which is the problems your buyer has around your offer: \"Why your profitable business has no cash\".',
         'Everyone, which means money, time, mindset and AI: \"How I think about money after looking at 200 companies\' books\".'])
para("Inayah sells an Airbnb course, but her biggest video is about money mindset, which is the outer ring. It's told through her own story, so the people who watch it end up on her Airbnb masterclass anyway.")
para("Clover Trading taught us the other side of this. Their psychology video, \"9 Years of Trading Experience in 31 Minutes\", got 16,963 views and booked 30 calls, but only made 1 sale. Their strategy video, \"This 'Stupid Simple' Setup Is The FASTEST Way To Become Profitable\", got about half the views and made more money than the other two videos we were testing combined.")
para("So wider topics bring in more people, and topics closer to your offer bring in buyers. You need both, and I'll show you how to mix them in the section on giving every video a job.")
h2("What's Working Right Now")
para("The tracking we run for clients follows each sale back to the exact video that started it. Across 207 channels, 26,621 videos and over 336 million views, it has traced more than $35 million in sales. A few things stood out about which ideas bring in money:")
bullets(['About a quarter of all the YouTube revenue we track came in the last 30 days, and the fastest-growing topic is AI and automation. If you can honestly talk about doing more with fewer people, that topic is moving in your favor right now.',
         'Views and money barely line up. The 100 videos that made the most money had a median of about 25,000 views. So you don\'t need a viral topic to make money from a video.',
         'Ideas built on something you did beat ideas that only teach. I\'ll come back to this in Step 3, because it\'s the whole reason the unique advantage matters.'])
para("**Try this:** write down 10 questions from your last few sales calls. Then do the Popular tab exercise on 5 channels. Circle the topics that show up in both lists.")

# ================= STEP 2 FORMATS =================
h1('Step 2: Steal A Format That Already Works')
para("I don't brainstorm ideas. I steal formats. I'm not stealing anyone's video, I'm adapting what already works.")
para("The way you find a format that works is by looking for **outliers**. An outlier is a video that did far better than that channel's usual videos. If a channel normally gets 5,000 views and one video gets 50,000, that's a 10x outlier, and something about the idea is working.")
para("The free vidIQ browser extension shows this number under every video. Without it, divide the video's views by the average of that channel's last 10 videos.")
h2('How Big An Outlier Has To Be')
para("The smaller the channel, the bigger the jump needs to be before you trust it:")
table([["Their channel size", "Counts as a win at"],
       ['Under 10,000 subscribers', '10x their usual views or more'],
       ['10,000 to 100,000', 'About 7x or more'],
       ['100,000 to 250,000', '5x or more'],
       ['250,000 and up', '2x or more']], [3.25, 3.25])
para("One outlier can be luck. **Two outliers on the same format is a pattern**, and a pattern is what you want to steal. Leila had two videos on \"How I Brainwashed Myself to ___\", and that's why we trusted it.")
para("The age of the video doesn't matter much. Leila's first one was about two years old when we used it. What matters is whether recent videos using the same format are still doing well. If you see a format everywhere and the newest ones are flopping, people are tired of it, so skip it for a few months.")
h2('Where To Look')
para("Look in this order:")
para("**1. Bigger channels your buyers already watch.** This is where Inayah's format came from. Leila has a big female audience, and so does Inayah. Same audience, same psychology, so the same title shape pulls the same people.")
para("If your buyers are business owners, that might be Alex Hormozi or Codie Sanchez. If they're CFOs or sales leaders, you might not know yet. Two ways to find out: ask your 3 best clients which YouTubers they watch, or search YouTube for their job title plus their problem (\"sales manager hiring\", \"CFO cash flow\") and note which channels show up more than once.")
para("**2. Your own niche.** For Clover Trading, we studied 764 videos across 28 trading channels before we made anything. Our first video, \"How I Used the Law of Detachment To Make Millions in Trading\", got 16,950 views on a channel that had been stuck around 1,000 a video for years. It became the channel's best long video ever.")
img('clover_study.jpg', 5.5, caption='(Our study of the trading niche before Clover\'s first video.)')
para("**3. Completely different niches.** When I made my YouTube scriptwriting course, every scriptwriting video out there was 9 to 11 minutes long. Meanwhile, in the dropshipping world, there were videos titled things like \"Full Dropshipping Course (18 Hours)\" doing really well. So I borrowed that format and made a 90-minute scriptwriting course. It's my most viewed video, with 312,439 views.")
para("**4. Your own channel, once you have a few videos.** A year later, I made that course again, this time 4 hours long. It became my second most popular video. If something worked for you once, there are usually more videos hiding in it.")
h2('Translate It One Step More Specific')
para("When you borrow a format, the topic you put in the blank has to make sense. \"The Full Guide To Marketing\" is too broad to work. \"The Full Guide To Getting Clients From LinkedIn\" can.")
para("If the format doesn't translate cleanly, don't force it. \"Bookkeeping Isn't Hard. It's Misunderstood\" works. \"Lawn Mowing Isn't Hard. It's Misunderstood\" sounds like a joke.")
h2('Free Tool: The YouTube Master Tracker')
para("We keep every outlier we find in one spreadsheet, so we can spot formats that keep showing up. You can make a copy of ours here: [[YouTube Master Tracker (Make A Copy)|https://docs.google.com/spreadsheets/d/1PCJiUpGoqg7j2ire5Idh_GMvLKTGH-LwCrIndRkF_Z4/edit?gid=589751072#gid=589751072]]")
para("**Try this:** pick 3 big channels your buyers watch. Open their Popular tab and write down every title shape that shows up twice. Ignore the topic and keep the shape.")

# ================= 10 FORMATS =================
h1('10 Formats That Worked For Our Clients')
para("To save you some time, here are 10 formats that worked on channels we've worked with, plus what each one could look like for a consultant or a CFO.")
table([['Format', 'Our example', 'Your version'],
       ['1. How I [did something] at/in [specific]', 'How I Brainwashed Myself to Be a Millionaire at 20 (1,203,773 views)', 'How I Rebuilt 40 Sales Teams in 6 Years'],
       ['2. I Make $[X] Per Month [doing Y] With One Simple [Z]', 'I Make $45k Per Month Trading One Simple Strategy (539,372 views)', 'This One Pricing Change Made My Client $20,000 A Month'],
       ['3. I Finally Revealed My Most Effective [X] (For Free)', 'I Finally Revealed My Most Effective Scalping Strategy (For Free) (about 10 booked calls)', 'I Finally Revealed My Cash Flow Template (For Free)'],
       ["4. If I Started [X] Again In [year], This Is Exactly What I'd Do", 'If I Started Trading Again In 2026 (about 200 webinar sign-ups in 72 hours)', "If I Started My Consulting Business Again In 2027, This Is Exactly What I'd Do"],
       ['5. This "[Simple]" [X] Is The Fastest Way To [result]', 'This "Stupid Simple" Setup Is The FASTEST Way To Become Profitable (our best seller for Clover)', 'This "Boring" Follow-Up Email Is The Fastest Way To Close Deals'],
       ['6. [X] Years Of [Y] Experience In [Z] Minutes', '9 Years of Trading Experience in 31 Minutes (30 booked calls)', '15 Years Of CFO Experience In 30 Minutes'],
       ['7. [X] Is Easy, Actually', 'getting rich is easy, actually (923,776 views)', 'Closing Big Clients Is Easy, Actually'],
       ['8. Full [X] Course ([length])', 'Full YouTube Script Writing Course (1+ Hour) (312,439 views)', 'Full B2B Sales Course (2 Hours)'],
       ['9. How To Start A [X] In [year] (Free Course)', 'How to Start an Ecommerce Business in 2025 (FREE COURSE) (447,211 views)', 'How To Start A Bookkeeping Business In 2027 (Free Course)'],
       ['10. If You Understand [X], You Understand [Y]', 'If You Understand Math, You Understand Trading (3 booked calls in 5 days)', 'If You Understand Your Bank Statement, You Understand Your Business']],
      [2.0, 2.4, 2.1])
img('formats_a.jpg', 6.0)
img('formats_b.jpg', 6.0)
para("Two things to notice. First, a lot of the formats that made money have a real number or a real result in them, which only works if it's true for you. Second, the videos that booked the most calls weren't always the ones with the most views. Scott's \"If You Understand Math\" video was him drawing on an iPad with no editing, and it booked 3 calls in its first 5 days.")
para("Don't try all 10. Pick 2 or 3 that fit what you can honestly say, and start there.")

# ================= STEP 3 ADVANTAGE =================
h1('Step 3: Make It Yours With Your Unique Advantage', page_break_before=True)
para("This is the step almost everyone skips, and it's the one that made Inayah's video work.")
para("When we started with Inayah, almost everyone in her niche was leading with the same thing, which was an income claim. \"How I made $10 million.\" \"My $50,000 a month Airbnb portfolio.\" There are thousands of people on YouTube calling themselves millionaires, so when everyone says it, nobody stands out.")
para("So I asked what Inayah could say that nobody else in her niche could. The answer was her age. Lots of people claim to be millionaires. Very few can say they did it at 20. She also had her story: she grew up in a big family without much money, and at one point 12 of them lived in a three-bedroom house. Nobody else can tell that story either.")
para("Take \"at 20\" out of the title and it's just Leila's video again. Put it back in and it's a video only Inayah can post. In the first month it hit 309,000 views, about 11 times her usual video, and it's now past 1.2 million.")
h2('Why This Matters For Sales')
para("Our tracking backs this up. Titles about something the creator *did* bring in far more money than titles that only teach:")
bullets(['\"How to\" titles get about a third of all the link clicks we track, but less than a fifth of the money.',
         'Titles in the first person (\"I\", \"my\") get 37% of the clicks and 52% of the money.',
         'Titles with a specific dollar amount get 34% of the clicks and 51% of the money.',
         'Titles framed as a question bring in less than 1% of the money.'])
para("A \"how to\" video teaches people for free, and once they've learned it they leave. An \"I did this\" video shows them you can do it, so the people who want it done for them reach out. Ethan's \"I Make $45k Per Month Trading One Simple Strategy\" is a good example, with 539,372 views.")
img('ethan_popular.jpg', 6.5, caption='(Ethan\'s Popular tab. The 539,372 and 154,885 view videos are two we worked on.)')
para("As I like to say, no one can copy your proof.")
h2('Five Kinds Of Unique Advantage')
table([['Kind', 'Example'],
       ['A result', '"I took a client from $0 to $1 million in sales in 14 months"'],
       ['A number', '"I\'ve rebuilt 40 sales teams" or "I\'ve read 200 companies\' books"'],
       ['An age or a timeline', '"Millionaire at 20" or "Retired 3 years early on a teacher\'s salary"'],
       ['A backstory', '"I got fired, then signed my old boss as a client"'],
       ['An opinion you earned', '"After 200 clients, I think most businesses don\'t need a CFO"']], [1.9, 4.6])
para("Now, you might be thinking: \"Bryan, my clients are under NDA, and my numbers aren't that big.\"")
para("That's normal for consultants and CFOs. You can still use the count (\"40 sales teams\"), the timeline (\"in 6 years\"), a before and after without names (\"a 12-person agency that was 3 weeks from running out of cash\"), or an opinion you earned from the work. You don't need a huge number. You need a specific one.")
h2('The Search Test')
para("Before you lock in a title, type it into the YouTube search bar. If someone else already has it, or could honestly post it, make it more specific. Search Inayah's title and you only find her, because nobody else can honestly say it.")
para("**Try this:** answer three questions in writing. What have you done that most people in your niche haven't? What's the most specific number attached to it? And what's the story behind that number?")

# ================= STEP 4 GRID =================
h1('Step 4: Mix Them Into 25 Ideas In 10 Minutes', page_break_before=True)
para("This is the fastest way I know to fill a content calendar. Write 5 topics down the left side and 5 formats across the top. Every box is an idea. That's 25 ideas from one sheet of paper.")
para("Here's part of the grid for a sales consultant:")
table([['Topic', 'If I Started ___ Again In 2027', '___ Is Easy, Actually', 'I Finally Revealed My ___ (For Free)'],
       ['Cold calling', "If I Started Cold Calling Again In 2027, This Is Exactly What I'd Do", 'Cold Calling Is Easy, Actually', 'I Finally Revealed My Cold Call Script (For Free)'],
       ['Follow-up', "If I Started Following Up Again In 2027, I'd Do This", 'Following Up Is Easy, Actually', 'I Finally Revealed My 5-Email Follow-Up (For Free)'],
       ['Hiring salespeople', "If I Hired My First Salesperson Again In 2027, I'd Do This", 'Hiring Great Salespeople Is Easy, Actually', 'I Finally Revealed My Sales Hiring Test (For Free)'],
       ['Pricing', "If I Set My Prices Again In 2027, I'd Do This", 'Raising Your Prices Is Easy, Actually', 'I Finally Revealed My Pricing Sheet (For Free)']],
      [1.3, 1.8, 1.6, 1.8])
para("Some of those boxes are weak, and that's fine. You're not trying to make every box a video. You're trying to find the 3 that make you think \"I'd click that\".")
para("Then add your unique advantage to those 3. \"Cold Calling Is Easy, Actually\" becomes \"I've Trained 40 Sales Teams. Cold Calling Is Easy, Actually.\" Now it's yours.")
para("**Try this:** fill in a 5 by 5 grid with your topics from Step 1 and your formats from Step 2. Circle your best 3 and add your advantage to each one.")

# ================= ONE JOB =================
h1('Give Every Video One Job')
para("Before you film anything, decide what the video is for. One video can't do everything, so give it one job.")
bullets(['Reach videos bring new people in. Wider topic, bigger promise. Inayah\'s money mindset video is a reach video.',
         'Sales videos turn watchers into buyers. A topic close to your offer, with real depth. Clover\'s \"Stupid Simple\" strategy video is a sales video.',
         'Search videos answer something people type into YouTube, so they keep getting found for years. Fiction Profits Academy is the top result for \"how to start a KDP business\".'])
img('fiction_search.jpg', 6.5)
para("Scott Taylor is a good example of why you need more than one job. We started him on sales videos, like a live backtest of his strategy. They only got 3,000 to 4,000 views, but the first few booked around 7 calls. The problem was that not enough new people were finding him.")
para("So we added reach videos tied to his funnel. \"I Finally Revealed My Most Effective Scalping Strategy (For Free)\" got 37,343 views in its first stretch, his biggest video in over a year, and booked about 10 qualified calls.")
img('scott_37k.jpg', 6.0)
para("A simple mix to start with: make 8 out of every 10 videos for people who could buy from you (sales and search), and use the other 2 to test something wider. If your sales videos convert but too few people see them, which was Scott's problem, add more reach videos.")
para("And to find out which videos actually sell, ask every new lead which video they watched. Write it down. After a month, that list will tell you more than your view counts.")

# ================= SCORE =================
h1('Score Every Idea Before You Film It')
para("I like to generate 100 ideas, cut them down to the best 20, then the best 5, and then make the one I'm most confident in. To do that cut quickly, score each idea out of 10 on five questions:")
table([['Question', 'What a 10 looks like'],
       ['1. Is the topic proven?', 'It\'s in the top videos of 3+ channels, or your prospects ask about it every week'],
       ['2. Is the format proven?', 'It\'s been an outlier at least twice, and recent copies still do well'],
       ['3. Is it mine?', 'You searched it on YouTube and nobody else could honestly post it'],
       ['4. Would a buyer click it?', 'If it took off, the people watching are people who could pay you'],
       ['5. Do I have 5 things to say they haven\'t heard?', 'You can write 5 points a viewer in your niche hasn\'t heard before']], [2.6, 3.9])
para("Add up the five scores:")
bullets(['40 to 50 means film it.',
         '30 to 39 means fix the lowest score first, then film it.',
         'Under 30 means bin it and move on.'])
para("Question 5 is the one people skip. If you can't write 5 points someone in your niche hasn't heard a hundred times, the video will feel like every other video on the topic, and people won't finish it. When that happens, keep researching or pick another idea.")

# ================= ROUTINE =================
h1('Your Weekly Idea Routine', page_break_before=True)
para("Ideas are a volume game. The more you look, the better the ones you keep. Here's the simplest routine I'd start with.")
h2('Set Up An Idea Bank')
para("Make one Google Doc with four headings:")
bullets(['Topics, from sales calls, the Popular tab and comments',
         'Formats, meaning every outlier title shape you\'ve seen work twice',
         'Ideas, which are your grid results, each with the title and the video that inspired it',
         'Shortlist, which is your best 5, ranked, with the top one next to film'])
h2('The Minimum Version')
para("Once a week, block 30 minutes. Add 10 new ideas to the bank, score them, and move the best one to the top of your shortlist. Film the top one. If you post one video a week, 10 good ideas is two and a half months of content.")
h2('When One Pops, Make The Next One Close To It')
para("When a video does far better than your usual, YouTube will show your next video to the people who liked it. So don't change direction. Make the next one about something close by.")
para("After Clover's \"Law of Detachment\" video took off, we followed it with \"I Used the Law of Attraction to Make +$8M Day Trading\". It got 12,000 views, which was also way above where the channel had been.")
img('followup.jpg', 6.0)
para("When you rank your shortlist, put anything time-sensitive first, like news in your industry. After that, pick the idea with the strongest proof or the one you're most excited to make. If you're not excited about it and you've got nothing new to say, cross it off.")

# ================= CHECKLIST =================
h1('Your Banger Idea Checklist', page_break_before=True)
para("Run every idea through this before you script it:")
checklist(['The topic came from a sales call, a competitor\'s Popular tab or their comments',
           'The format has been an outlier at least twice, and recent copies still work',
           'The title has my unique advantage in it',
           'I searched the title on YouTube and nobody else could honestly post it',
           'I know if this video\'s job is reach, sales or search',
           'I have at least 5 points my viewer hasn\'t heard before',
           'It scores 40 or more out of 50'])

# ================= CTA =================
h1('Want Us To Do This For You?')
para("This is what we do every week at Viral Bangers. We find the topics, steal the formats, dig out your unique advantage and write the scripts. You approve the ideas and hit record.")
cta_link('viralbangers.com', 'https://viralbangers.com')
