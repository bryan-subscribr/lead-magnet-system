# TIKTOK lead magnet: "The TikTok-to-YouTube Playbook". Voice: Bryan Ng. Data pulled 29 Oct 2026 (vidIQ, Nexlev, Subscribr Strategy Search).
NAV_S = 'https://www.youtube.com/shorts/julmRjiSasM'
NAV_L = 'https://www.youtube.com/watch?v=GHrhzZv_MwQ'
NAV_T = 'https://www.tiktok.com/@simonsquibb/video/7669456900089531670'
COD_S = 'https://www.youtube.com/shorts/RU6yYP1RjDI'
COD_L = 'https://www.youtube.com/watch?v=CSSUx4TuGug'

title_page('The TikTok-to-YouTube Playbook',
           [('Turn The TikToks That Already ', False), ('Worked', True), (' Into 12-Minute Videos That Pay', False)],
           hero='hero.jpg')
toc_page(levels=1)

# ================= TL;DR =================
h1('TL;DR')
para("Most people pick their YouTube ideas by guessing. You don't have to. If a TikTok, Reel or Short already blew up, the audience has voted on that idea, and it's sitting right there in your analytics (or in someone else's).")
para("This guide shows you how to take a short video that already proved an idea and turn it into a 12-minute YouTube video. That longer video pays a lot more per view, it builds way more trust, and if you run a business, it's the video that gets people to book a call.")
para("Simon Squibb is the cleanest example I found. In January 2026 he posted a 59-second Short about a chef called Nav. It got 2,918,783 views. Three months later he turned the same story into a 13:57 video, which has 559,109 views. Then in August his TikTok update on Nav did 30.1 million views.")
img('nav_three_formats.jpg', 6.5, caption='(Same story, three formats: the Short, the long video, and the TikTok update.)')
para("The long video got fewer views. But using vidIQ's average rates, those 559,109 long-form views are worth around $4,473 in ads, and the 2.9 million Short views are worth around $467. That's about 5 times fewer views for around 10 times more money.")
para("In this doc you'll get:")
bullets(["Real examples from Simon Squibb and Codie Sanchez, with views and dates for the short and the long version side by side.",
         "What 1,000 views actually pays on Shorts vs long videos, with numbers from creators who showed their dashboards.",
         "The 6-step playbook: find a proven TikTok, score it, turn the hook into a title and thumbnail, expand 60 seconds into a 12-minute outline (with a fill-in template), film it, and link the Short to the long video.",
         "How a business owner uses this, starting with the Reels that already got you DMs.",
         "A checklist you can run every week."])

# ================= WHO WE ARE =================
h1('Who We Are')
para("My name is Bryan, and I run Viral Bangers with my co-founder Mauricio. We're a YouTube agency for business owners who sell something, like coaches, consultants, traders and info product businesses. We handle the ideas, scripts, editing and thumbnails, so all you have to do is show up and record. One of the creators we work with is Brad Goh (The Trading Geek), who has over 1.8 million subscribers on YouTube.")
para("Here are a few of the people we've worked with:")
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

# ================= WHY =================
h1('Why A TikTok That Already Worked Is Your Best Video Idea')
para("A long YouTube video takes real work. Research, a script, a day of filming, editing, a thumbnail. If the idea is bad, all of that goes in the bin. A short video is cheap to make, so it's the perfect place to test an idea before you spend a week on it.")
para("Oscar Owen says it pretty directly in his video on Shorts: post short videos often, see which ones beat the rest, and build your long videos on the winners. He says it cuts the risk of \"spending a week producing a video that ultimately flops.\" Think Media calls TikTok a sandbox for the same reason. If something hits there, people care about that topic.")
para("I broke down Simon Squibb's channel on my own channel a while back, and his story is the TikTok-to-YouTube story in one person. Before his YouTube blew up, he already had 500,000 followers on TikTok, asking strangers \"what's your dream?\"")
img('bryan_simon_tiktok_profile.jpg', 3.2, caption='(Simon\'s TikTok when I broke down his channel: 500,000 followers and 109.5 million likes.)')
para("But as I said in that video, there's only so much you can teach in a 30 to 60 second TikTok. At best it's one lesson, and it's mostly entertainment. To actually make an impact and get people to take action, he needed long videos on YouTube.")
img('bryan_simon_breakdown.jpg', 6.0, caption='(From my breakdown of Simon\'s "30 Years of Business Knowledge in 2hrs 26mins", which now has 18,029,077 views.)')
para("Once he went long, one video took his channel from averaging about 5,000 views to about 300,000 across his next 10 uploads. Today his channel has 2.48 million subscribers.")
para("And look at where his views still come from. Nexlev shows 85% of all his YouTube views are on Shorts. The Shorts bring the reach, and the long videos bring the money and the trust.")
img('chart_simon_split.jpg', 6.0)
para("**Try this:** open TikTok, Instagram or YouTube Studio and sort your own short videos by views. Write down your top 10. Those are your first 10 long-video ideas.")

# ================= MONEY =================
h1('What 1,000 Views Pays On Shorts vs Long Videos')
para("Quick definition first: RPM means revenue per mille, which is what you actually keep from every 1,000 views after YouTube takes its cut.")
para("Shorts and long videos are paid in totally different ways. On a long video, ads play before and inside your video, and you get a share of those ads. On Shorts, ads play between Shorts in the feed. YouTube puts that money in a pool, takes out music licensing first, and splits the rest by how many plays each creator got. Think Media explains that creators get 45% of their share. Nate Black points out that the length of your Short doesn't matter for that split, only the number of plays.")
para("These are numbers creators have shown from their own dashboards:")
table([['Creator', 'What they showed', 'Per 1,000 views'],
       ['Aprilynne Alter', '1,000,000 Shorts views pays about $60', 'Shorts $0.06'],
       ['Oscar Owen', 'One Short with 50 million views paid about $1,700', 'Shorts about $0.03'],
       ['Think Media', 'An 11.2 million view Short paid $536.74', 'Shorts $0.06, long $7.36'],
       ['Think Media', '14 million Shorts views paid $2,351. 390,000 long views paid $5,172', 'Long about $13'],
       ['Grow With Kaz', 'Same cooking niche', 'Shorts $0.03, long $11.25']],
      [1.4, 3.6, 1.5])
img('aprilynne_60_dollars.jpg', 5.5, caption='(Aprilynne Alter: $60 takes 1,000,000 Shorts views, or about 24,000 long-form views at a $2.50 RPM.)')
img('chart_creator_rpm.jpg', 6.0)
para("I also ran both formats through vidIQ's earnings calculator for a business channel with a US audience. One million long-form views comes out at around $8,000. One million Shorts views comes out at around $160. That's 50 times more for the same number of views.")
img('chart_1m_views.jpg', 6.0)
para("To be fair to Shorts, they're great for getting subscribers. Oscar Owen's 50 million view Short paid about $1,700, but it also brought in 124,000 subscribers. So keep making short videos. Use them to find ideas and get attention, and let the long videos do the earning.")
h2('Why 12 Minutes, And Not 4')
para("Once a video is 8 minutes or longer, you can put ads in the middle of it (mid-rolls). Make Money Matt shows how to add them in YouTube Studio under Content, then Monetization, then Manage mid-rolls, and suggests spacing them about every 2 minutes. Grow With Kaz says an 8-minute video will usually earn a higher CPM than a 7-minute one for exactly this reason.")
para("I'd still aim for 12. A 12-minute video gives you room for 4 or 5 mid-rolls without them feeling spammy, and it sits right in the range that does well for teaching videos. Nate Black calls 12 to 16 minutes the stretch zone for teacher and commentary channels. In one of our Subscribr Academy calls, the top 10% of education videos averaged 16:58, and health videos 13 to 14 minutes.")
para("There's one catch. Make Money Matt warns not to pad a video just to add ads. If people leave because you're stretching it, the video dies anyway. Every minute has to earn its spot, which is what the outline step below is for.")

# ================= EXAMPLE 1 =================
h1("Real Example: Simon Squibb's 59-Second Short That Became A 14-Minute Video")
para("This is the one I'd study if you only study one. Same chef, same café, same deal, told in three formats.")
img('nav_pair.jpg', 6.5, caption='(Left: the Short, 26 Jan 2026, 2,918,783 views. Right: the long video, 29 Apr 2026, 13:57, 559,109 views.)')
table([['', 'Short', 'Long video', 'TikTok update'],
       ['Title or hook', '"Her food was SO good... I offered to buy the place"', '"She Made Me The Best Pasta Ever, So I Bought Her A Restaurant"', '"I was so angry! HUGE UPDATE"'],
       ['Length', '59 seconds', '13:57', '85 seconds'],
       ['Posted', '26 Jan 2026', '29 Apr 2026', '2 Aug 2026'],
       ['Views', '2,918,783', '559,109', '30.1 million'],
       ['Ad money (estimate)', 'About $467', 'About $4,473 (Nexlev says $6,944)', 'Not on YouTube']],
      [1.3, 1.7, 1.9, 1.6])
img('chart_nav_pair.jpg', 6.0)
para(f"Links if you want to watch them: [[the Short|{NAV_S}]], [[the long video|{NAV_L}]], [[the TikTok|{NAV_T}]].")
h2('The Short Is Built To Make You Want Part 2')
para("Watch how the Short ends. Simon makes the café owner an offer of $25,000, and the last line is \"But would they accept it and make Navasarat's dream come...\" and it cuts off. At 14 seconds in, there's even a sticker on screen that says \"Part 2 incoming.\"")
img('nav_short_beats.jpg', 6.5, caption='(The Short: "Remember her?" at the start, "Part 2 incoming" at 0:14, and a cliffhanger at the end.)')
para("That's exactly what Think Media's interview with a YouTube employee recommends for moving Short viewers to long videos: open a loop in the Short that only the long video closes.")
h2('What He Added To Get From 59 Seconds To 13:57')
para("I went through the whole transcript of the long video (2,873 words). The meeting in the Short only takes the first minute or so. Everything after that is new. This is the timeline:")
table([['Time', 'What happens'],
       ['0:00', 'Stakes up front: "I\'m willing to bet $50,000 on this under-confident chef." He only has 4 days left in New Zealand.'],
       ['0:36', 'The same meeting from the Short: "best pasta I\'ve ever had", "what\'s your dream?"'],
       ['1:08', 'The problem: the café is for sale for around $67,000 to $68,000, and rent, rates and staff are hard.'],
       ['1:41', 'Backstory: all her savings went to helping her family.'],
       ['2:12', 'Challenge 1: write a menu overnight, then cook 5 dishes in 30 minutes for a taste test.'],
       ['4:23 to 6:03', 'What\'s really holding her back: "I am such a boring person." She nearly quit cooking.'],
       ['6:03 to 7:06', 'The owner, Nancy, reveals she already offered Nav the café twice. Monthly payments are a no because of old debt.'],
       ['7:38', 'Challenge 2: a MasterChef judge pushes her to think like an owner ("the extra 5% magic").'],
       ['9:14', 'Sponsor read.'],
       ['10:19', 'Simon offers $25,000 cash, 24 hours to decide.'],
       ['11:23', 'Twist: agent fees push the real price close to $50,000, with 10 hours until his flight.'],
       ['12:30 to 13:57', 'Final price $50,000, deal done with under an hour left, logo reveal, café open.']],
      [1.1, 5.4])
para("Notice the clock. He reminds you how much time is left in almost every section: 4 days, then 3, then 2, then 24 hours, then 10 hours, then 1 hour. That one device keeps you watching for 14 minutes.")
img('nav_countdown.jpg', 6.5, caption='(The countdown comes back again and again: 3 days, 2 days, 23:59:59, and the price jumping to $50,000.)')
img('nav_long_timer.jpg', 5.5, caption='(Challenge 1: a 30-minute timer on the taste test.)')
img('nav_long_backstory.jpg', 5.5, caption='(The backstory the Short had no time for: "So all of my savings went to them.")')
img('nav_long_selfbelief.jpg', 5.5, caption='(He even tracks her "self-belief" with a bar on screen.)')
para("So the long video answers every question the Short raised: why didn't she do it already, what does it cost, what could go wrong, and did it actually work.")
img('nav_long_endcard.jpg', 4.5, caption='(The last frame of the long video points people to Nav\'s café and her own accounts.)')
img('tiktok_nav_pair.jpg', 5.0, caption='(The TikTok update, 2 Aug 2026: 30.1 million views, 47.1 times his usual TikTok views according to vidIQ.)')

# ================= EXAMPLE 2 =================
h1('Real Example: Codie Sanchez And The Vending Machine Short')
para("Codie Sanchez sells business-buying education, so her channel is a good model if you sell something. In April 2022 she posted a 59-second Short about a guy called Quinn who runs vending machines. It has 11,198,288 views.")
img('codie_short_beats.jpg', 6.0, caption='(The Short: the result in the first second, the cost breakdown, then a newsletter ask.)')
para("The Short is a perfect list of questions waiting for a long video. In under a minute it throws out: $15,000 a month in revenue, $9,750 profit, 27 machines, about 10 hours a week, about $2,100 all-in per machine, where the machines go, what goes in them, and the software that runs it. Every one of those is a section.")
para("In March 2025 she made the long version, \"I Bought 3 Vending Machines... My Earnings SHOCKED Me!\". It's 23:33 long and has 2,272,449 views. Instead of telling Quinn's story again, she tested it herself. That's a smart way to go long: the Short says it works for someone else, the long video shows whether it works for you.")
img('codie_vending_pair.jpg', 6.5, caption='(Left: the Short, 5 Apr 2022, 11,198,288 views. Right: the long video, 9 Mar 2025, 23:33, 2,272,449 views.)')
para(f"Watch them here: [[the Short|{COD_S}]] and [[the long video|{COD_L}]]. She even made a second long video on the same idea in July 2025, where her producer runs the machines for 30 days. When an idea keeps working, keep going back to it.")
h2('It Works In Both Directions')
para("Her long video \"Businesses that Never Fail? 6 Businesses with Amazingly Low Failure Rates\" came first, in September 2022, and has 5,888,060 views. Almost two years later she posted a Short called \"6 Businesses That Rarely Fail\", and it has 6,719,311 views. So once you have both, the long video feeds Shorts and the Shorts feed the long video.")
img('codie_6biz_pair.jpg', 6.0, caption='(Long first this time: 7 Sep 2022, 5,888,060 views. The Short came on 1 Aug 2024 and has 6,719,311 views.)')
para("One more thing I noticed. Her Short \"How gas stations really make money\" (June 2025) has 9,705,017 views and a vidIQ outlier score of 118, meaning it did over 100 times her normal. I couldn't find a long version of it on her channel. That's exactly the kind of gap you're looking for in your own niche.")

# ================= STEP 1 =================
h1('Step 1: Find The TikToks That Already Proved An Idea')
para("Start with your own videos, then look at your niche. Your own winners are the best place to start because the audience already likes you saying it.")
h2('Your Own Videos')
para("Sort your TikToks, Reels and Shorts by views. Then work out your normal. Take your last 10 videos and find the middle number. Anything doing 3 times that or more is a candidate, and anything at 10 times is a must-make. This is what people call an outlier: a video that did far more than your usual, which in my Strategy Search docs we measure against the average of your last 10 videos.")
h2('Other People In Your Niche')
para("Kallaway shows a free tool most people skip. Type \"Creator Search Insights\" into the TikTok search bar. It shows what people are searching for on TikTok in your category right now.")
img('tiktok_creator_search_insights.jpg', 5.0, caption='(From Kallaway\'s video: type "Creator Search Insights" in TikTok search, then browse by category.)')
para("He also suggests building a list of short-form creators in your niche and tracking what works for them, because the easiest way to make a winning video is to remix one that already won. Amplify Views says most short-form trends start on TikTok first, so that's where you look.")
para("The fastest way I know is an outlier search. vidIQ has one that searches TikTok and Instagram for posts that did way better than that creator's normal. When I searched for business owners, this one came up:")
img('bakery_reel_hook.jpg', 3.0, caption='(A bakery owner\'s Reel: 775,200 views, 417 times his normal 1,900, posted 25 Jul 2026.)')
para("The Reel is 7 seconds long. The text says \"As a 7-figure bakery owner, I probably shouldn't share this pricing formula...\" and the caption gives the formula: price equals ingredient cost divided by 0.30. The account has 15,100 followers and usually gets about 1,900 views. That's a proven idea with no long version yet. I'll use it as the worked example in Step 4.")
para("**Try this:** find 10 candidates. 5 from your own videos, 5 from your niche. Save the link, the views and the creator's normal views for each.")

# ================= STEP 2 =================
h1('Step 2: Score Them Before You Pick One')
para("Not every viral short makes a good long video. Think Media puts it well: a quick comedy sketch usually loses its punch when you stretch it, but teaching videos have room to grow. You can go deeper on one point, turn a quick fix into a full tutorial, or turn \"5 tips\" into 5 full sections with examples.")
para("Give each candidate a score out of 10 with this table:")
table([['Question', 'Score'],
       ['Did it do 3 times the creator\'s normal views? (10 times or more = 2 points)', '0 to 2'],
       ['Are people asking follow-up questions in the comments, or DMing about it?', '0 to 2'],
       ['Does the short leave obvious questions open (like how much it costs, or what happened next)?', '0 to 2'],
       ['Can you add something only you have, like your own numbers, clients or story?', '0 to 2'],
       ['Is it about something your buyer cares about?', '0 to 2']],
      [5.3, 1.2])
para("Make the 7s and up. Park the rest.")
para("Two quick filters from people who've gone viral a lot. Jenny Hoyos says on JeremyB's channel that if you can't explain the idea in under 10 words, don't make it. And Kevin Parry told Jay Clouse to test the idea with \"Have you seen the video where [blank] does [blank]?\" If you need a third blank, it's too complicated. \"Have you seen the video where Simon buys a chef her café?\" passes easily.")
para("One more from Kallaway, which he calls the share test: send the short to a friend who's exactly your buyer. Would they send it on to someone else? If yes, it's worth going long.")
para("**Try this:** score your 10 candidates and circle the top 3.")

# ================= STEP 3 =================
h1('Step 3: Turn The Hook Into A Title And Thumbnail')
para("The TikTok hook was written to stop a thumb in a feed. A YouTube title has a different job. Someone sees it next to 20 other videos and has to choose yours. So keep the same idea, but make the title promise the whole story or the full result.")
table([['Short hook', 'Long title', 'What the thumbnail shows'],
       ['"Her food was SO good... I offered to buy the place"', '"She Made Me The Best Pasta Ever, So I Bought Her A Restaurant"', 'Simon and Nav at the table, a plate of food, 5 gold stars'],
       ['"Wanna make $10K/ Month with Vending Machines?"', '"I Bought 3 Vending Machines... My Earnings SHOCKED Me!"', 'Codie, a vending machine, a fan of cash, "DAY 9"'],
       ['"How To Quit Your Job And Start A Business!"', '"How To Quit Your Job (And Do What You Love)"', 'Simon and Ali Abdaal, "Thank me in 12 months..."'],
       ['"As a 7-figure bakery owner, I probably shouldn\'t share this pricing formula..."', 'Example: "The Pricing Formula Behind Our 7-Figure Bakeries"', 'The owner in the kitchen, one product, its price tag']],
      [2.0, 2.4, 2.1])
img('simon_quit_pair.jpg', 6.0, caption='(Simon\'s older pair: the Short, 29 Dec 2022, 2,859,972 views, then the 57:01 video with Ali Abdaal, 16 Apr 2025, 417,599 views.)')
para("Simon did the same thing with his biggest video. In my breakdown, I showed how he took a proven title format from other channels (\"X years of knowledge in X minutes\") and a proven thumbnail ($0 on the left, $1m on the right) and made them his own. That's 18,029,077 views on a title and thumbnail he didn't have to invent.")
img('simon_30years_thumb.jpg', 5.0, caption='("30 Years of Business Knowledge in 2hrs 26mins", 27 Mar 2024, 18,029,077 views.)')
para("Then make the first 5 seconds of the video confirm the title. As I said in my hooks video, the first job of your intro is to show people they clicked on the right video. Paddy Galloway says the same: if the thumbnail shows a drone, show the drone in the first 3 seconds.")
para("**Try this:** for each of your top 3, write 3 title options and one sentence describing the thumbnail. Pick the one you'd click if it wasn't yours.")

# ================= STEP 4 =================
h1('Step 4: Expand 60 Seconds Into A 12-Minute Outline')
para("This is where most people mess up. They take a 60-second idea and just talk slower. The way to go long is to answer every question the short left open, and add the stuff only you know.")
para("Marcus Jones says it well: take viewers through the whole process. Show the setup, the problems, the steps and the reasoning along with the final result. In my 4,000 watch hours video I said the same about story: add more story beats and show more of how it felt. That's exactly what Simon did with Nav.")
para("Your extra 11 minutes come from 4 places:")
bullets(["Depth: the how. The steps, the numbers, the tools, the costs.",
         "Story: who it happened to, what was at stake, what went wrong, how it ended.",
         "Proof: screenshots, results, before and after, a real client.",
         "Questions: the comments under your short. Every \"but what about...\" is a section."], numbered=True)
h2('The 12-Minute Template')
para("Fill in the last column for your video:")
table([['Time', 'Section', 'What goes in it', 'Yours'],
       ['0:00 to 0:30', 'Hook', 'Say the TikTok hook again, then raise the stakes. Confirm the title in the first 5 seconds.', ''],
       ['0:30 to 1:30', 'Why it matters', 'Who this is for, what they get by the end, why you can talk about it.', ''],
       ['1:30 to 3:30', 'Part 1: the claim', 'The thing the short said, with proof.', ''],
       ['3:30 to 6:00', 'Part 2: the how', 'The steps and the numbers the short skipped.', ''],
       ['6:00 to 8:30', 'Part 3: the story', 'A real example: you, a client, a customer. What went wrong.', ''],
       ['8:30 to 10:30', 'Part 4: the questions', 'The top comments and DMs under the short, answered one by one.', ''],
       ['10:30 to 11:30', 'The payoff', 'The result, or the thing they can do today.', ''],
       ['11:30 to 12:00', 'Next step', 'Point to your next video, or your booking link if you sell something.', '']],
      [1.1, 1.3, 2.9, 1.2])
para("Between every section, put a re-hook. In my script template video I break it into three parts: say what they just got, hint at what's coming, and promise the next part is worth even more. Something like \"So now you know what to charge. But if you don't do this next part, you'll lose money on your best seller anyway.\"")
para("Adam Ivy says viewers decide whether to keep watching about every 60 to 90 seconds, which is why each section in the template is about 2 minutes. And Mario Joos suggests making your sections different lengths, so the video doesn't feel like the same beat over and over.")
h2('Worked Example: The Bakery Pricing Reel')
para("Say you own a bakery and that Reel was yours. It did 417 times your normal views. This is how the 7 seconds becomes 12 minutes. The brackets are where your real numbers go.")
table([['Time', 'Section', 'What you say or show'],
       ['0:00', 'Hook', '"As a 7-figure bakery owner, I probably shouldn\'t share this. This is the exact formula we use to price everything we sell." Show one product and its price.'],
       ['0:30', 'Why it matters', 'Most bakeries guess their prices. Here\'s what that cost us before we fixed it: [your real story].'],
       ['1:30', 'Part 1', 'The formula: price equals ingredient cost divided by 0.30. Work one real product through it, on screen: [your numbers].'],
       ['3:30', 'Part 2', 'Why 0.30 and not 0.25 or 0.40: [your reasoning]. What the formula doesn\'t cover, like labour, rent and packaging, and how you handle those.'],
       ['6:00', 'Part 3', 'A product you priced wrong, what happened, and what changed after you fixed it: [your story].'],
       ['8:30', 'Part 4', 'The top comments from the Reel: wholesale prices, premium items, what if my ingredients go up?'],
       ['10:30', 'Payoff', 'Price 3 of your own products live, start to finish.'],
       ['11:30', 'Next step', 'Link to your next video, or your offer if you help other bakeries.']],
      [0.8, 1.2, 4.5])
para("Every section is something a viewer of the 7-second Reel would actually want to know.")
para("**Try this:** take your top-scoring idea and fill in the template. If you can't fill a section with something real, cut it and make a 9 or 10-minute video instead. As I always say, make your video as long as it needs to be, but as short as it can be.")

# ================= STEP 5 =================
h1('Step 5: Film It')
para("You don't need a word-for-word script if you know the topic well. Oscar Owen films from bullet points with a simple structure he calls HIVE: a hook, a short intro, 3 to 5 value points, and an end screen. The template above already gives you those bullets.")
para("If you'd rather script it, script the first 30 seconds and the re-hooks word for word, and talk through the middle from bullets. The hook and the transitions are where people leave, so that's where the words matter most.")
para("Two things to do on the same filming day:")
bullets(["Film the new short pieces while you're set up. Every section of the long video can become its own Short later, which is exactly what Codie did with her 6 businesses video.",
         "Grab real proof on screen as you go: your dashboard, the product, the receipt, the client message. Proof is what makes a long video better than the short."])
para("Want us to just do this for you? This is literally what we do at Viral Bangers. We find the short videos that already worked, turn them into long videos, write the scripts, and handle the editing and thumbnails. If you'd like to see what that would look like for your channel, [[book a call here|https://www.viralbangers.com/book]].")

# ================= STEP 6 =================
h1('Step 6: Link The Short To The Long Video')
para("Once the long video is live, connect it to the Shorts. YouTube has a feature for this called Related video. Think Media walks through it:")
bullets(["Open YouTube Studio and go to your Shorts.",
         "Click the Short you want to edit.",
         "Find Related video and click it.",
         "Pick the long video from the list.",
         "Click Save."], numbered=True)
img('studio_choose_related_video.jpg', 6.0, caption='(The "Choose specific video" box in YouTube Studio, from Think Media\'s video.)')
para("Now there's a little link under the Short's title that takes people straight to the long video.")
img('short_related_link.jpg', 3.2, caption='(What it looks like on the Short: the linked video\'s title shows under the caption.)')
h2('What To Expect From It')
para("Be realistic here. Marcus Jones says only about 0.5% to 4% of Short viewers usually click through to a long video. Think Media found a Short with 10,000 to 20,000 views sent about 53 views, and a Short with 10 million views sent more than 3,000. Creators who use it well see their long-form views go up by roughly 10%.")
para("You can see why in your own analytics. Go to Analytics, then Content, and scroll to Viewers across formats. On Think Media Podcast's screen, 76% of returning viewers only watch videos, 12% only watch Shorts, and 12% watch both.")
img('studio_viewers_across_formats.jpg', 4.5, caption='(Viewers across formats on Think Media Podcast\'s channel.)')
para("Oscar Owen goes further and warns that on channels that post both, only about 11% of viewers watch both, and that posting tons of Shorts can drag down your long videos. One creator he talks about went from 1.2 million long-form views a month to 400,000 after starting daily Shorts.")
para("So treat the link as a bonus. The real plan is the long video getting found on its own through search and suggested videos, and the link catches the people who want more.")
h2('Make Them Want To Click')
bullets(["End the Short on an open question, like Simon's \"But would they accept it...\"",
         "Say it out loud or put it on screen: the full story is linked below the title.",
         "Reward the click. The first seconds of the long video should continue exactly what the Short promised, which is what Think Media's YouTube employee interview recommends."])
para("And if you're posting your TikToks as Shorts too, upload the clean file. Think Media warns that videos with another platform's watermark can get less reach, so post natively everywhere.")
para("**Try this:** the day your long video goes live, link it from every Short on the same topic, including the one that gave you the idea.")

# ================= BUSINESS =================
h1('How A Business Owner Uses This (Start With The Reels That Got You DMs)')
para("If you sell something, the score is DMs and booked calls. So your best short videos are the ones where people messaged you asking how much it costs or whether you can help, even if they didn't get the most views.")
para("Those DMs are the best signal you'll ever get, because they come from buyers. Turn those exact Reels and TikToks into your long videos.")
para("Why bother going long? Alex Hormozi tested this on his own channel. When he focused on long-form business content, his opt-ins went up 26% and his sales doubled, even with fewer views per video. He also said people tend to stick to the format they like, so Shorts viewers don't automatically turn into long-form viewers.")
para('I feel the same way. In one of my videos I said "I\'d rather have 1,000 people know me really well than 100,000 people having seen my face for only 5 seconds." As I put it in that video, "You want to be known well, not well known."')
img('bryan_known_well.jpg', 6.0, caption='(From my video "The NEW Way to Grow Your YouTube Channel in 2024".)')
para("Shane Hummus and Linden Chasteen both point to Google's research that buyers consume about 7 hours of content before a big purchase. You can't get anywhere close to that with 60-second videos. And Think Media shared the story of a Dallas real estate agent whose clients binge-watched 50 to 100 of his videos and then closed deals without ever meeting him in person.")
h2('What This Looks Like For A Service Business')
table([['The Reel that got DMs', 'The long video', 'Where it points'],
       ['"3 signs your ads are wasting money"', 'Walk through 3 real ad accounts and show where the money went', 'Book a free audit'],
       ['"What I\'d charge for this kitchen remodel"', 'Price a full remodel line by line, with the photos', 'Get a quote'],
       ['"The question I ask every new coaching client"', 'A full first session, start to finish (with permission)', 'Apply to work with you'],
       ['"How we cut our client\'s tax bill"', 'The full case: before, the changes, after, what it cost', 'Book a call']],
      [2.2, 2.6, 1.7])
para("Put your booking link in the first line of the description and in the last minute of the video. Someone who just watched 12 minutes of you is a very different lead from someone who saw you for 6 seconds.")
para("**Try this:** go through your DMs from the last 90 days. Write down which video each conversation came from. The video that shows up most is your next long video.")

# ================= MISTAKES =================
h1('Mistakes That Kill The Long Version')
bullets(["Padding. If the short was 60 seconds of value, 12 minutes of the same point stretched out will get clicked off. Add new depth, story and proof, or make it shorter.",
         "Switching topics. If the title promises the pasta story, don't spend the first 2 minutes on your life story.",
         "Copying word for word. Use the idea and the format, then put your own spin on it with your own numbers and examples. That's how Simon used other channels' title and thumbnail.",
         "Picking a joke. Sketches and memes usually don't stretch. Teaching, stories and results do.",
         "Judging the long video by the short's views. 559,109 views on a long video can earn more than 2.9 million on a Short.",
         "Only posting Shorts. They grow subscribers fast but pay little and convert worse for business. Use them to test ideas and point to your long videos."])

# ================= CHECKLIST =================
h1('The Checklist')
checklist(["Sorted my own TikToks, Reels and Shorts by views and found my normal (the middle of my last 10).",
           "Listed 10 candidates: 5 of mine, 5 from my niche (Creator Search Insights, outlier search, creator list).",
           "Scored each one out of 10 and picked a 7 or higher.",
           "Passed the 10-word test and the \"[blank] does [blank]\" test.",
           "Wrote 3 title options and picked the one I'd click.",
           "Described a thumbnail that shows the result or the story, and made the first 5 seconds confirm it.",
           "Filled in the 12-minute template with real depth, story, proof and comment questions.",
           "Cut any section I couldn't fill with something real.",
           "Wrote a re-hook between every section.",
           "Filmed extra short pieces and grabbed on-screen proof on the same day.",
           "Made the video 8 minutes or longer and placed mid-rolls about every 2 minutes.",
           "Linked every related Short to the long video with Related video.",
           "Uploaded clean files with no other platform's watermark.",
           "Put my booking link in the first line of the description and at the end of the video.",
           "Checked which videos my DMs came from and picked my next idea."])

# ================= CTA =================
h1('Want Us To Do This For You?')
para("If you've got short videos that already worked and no time to turn them into long videos, that's what we do. At Viral Bangers we find the ideas your audience already voted for, write the scripts, edit the videos, design the thumbnails, and set everything up so the views turn into calls. You just show up and record.")
para("**Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]")
