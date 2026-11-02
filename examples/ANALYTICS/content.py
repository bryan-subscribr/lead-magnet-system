# ANALYTICS lead magnet: "How To Read YouTube Analytics (My Full Guide)". Built 2026-10-29 with the lead-magnet-doc skill.
# Voice: Bryan Ng. Spine: Bryan's "Analytics system" doc, his Claude-course CTR testing section (qdE8FKQC_Vg ~2:02),
# the team's thumbnailtest.com SOP, and the client-tracking numbers Bryan approved for the ALGORITHM guide.
# Build: python3 ~/.claude/skills/lead-magnet-doc/scripts/docbuilder.py content.py "How To Read YouTube Analytics (My Full Guide).docx" --img-dir img

title_page('How To Read YouTube Analytics (My Full Guide)',
           [('The ', False), ('Only', True), (' Numbers I Check After Every Video', False)], hero='hero.jpg')
toc_page(levels=1)

# ================= TL;DR =================
h1('TL;DR')
para("YouTube Studio shows you about 50 numbers. I look at a handful of them, in the same order, every time I post. This guide is that order, with the screenshots, the benchmarks I use and what I change when a number looks bad.")
para("The short version is this. A lot of people treat click-through rate times average view duration as the magic formula for going viral. After reviewing a lot of videos, I've found the two numbers that tell me the most are the views a video has after 30 days, compared to what I expected from that idea, and how many people are still watching at 30 seconds. Almost everything else is there to help me figure out why one of those two came in low.")
para("I also check things at three moments: the first 24 hours, day 7 and day 30. Each check answers a different question, and each one has a different fix.")
para("And if you run a business, views are the wrong scoreboard anyway. In the tracking we run for clients, the 100 most viewed videos made only about 11% of the money. Near the end I'll show you the numbers I use to judge a video by leads and booked calls instead.")
img('bryan_study_analytics.jpg', 5.5, caption='(Me explaining why you need to study your analytics, in my 2025 growth video.)')

# ================= WHO WE ARE =================
h1('Who We Are')
para("My name is Bryan, and I run Viral Bangers with my co-founder Mauricio. We're a YouTube agency for business owners who sell something, like coaches, consultants, traders and info product businesses. We handle the ideas, the scripts, the editing and the thumbnails, and then we track which videos turn into booked calls. One of the creators we work with is Brad Goh (The Trading Geek), who has over 1.8 million subscribers on YouTube.")
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
para("I spend a lot of time in analytics for our clients' channels, for Subscribr's channel and for my own channel, which has 22,200 subscribers. What follows is how I actually read them.")

# ================= TWO NUMBERS =================
h1('The Two Numbers I Actually Care About')
para("A while ago I wrote my analytics system down in a one-page doc. It starts like this: everyone thinks the important metrics for going viral are click-through rate times average view duration. I've found that the only two numbers that really matter are the views after 30 days and the retention in the first 30 seconds.")
h2('1. Views After 30 Days, Compared To What You Expected')
para("It's too early to judge a video before 30 days are up. The one exception is when the views graph goes completely flat, because then I know the video isn't going to do anything.")
para("And I never judge the raw number. I judge it against what I expected from that specific idea. On my channel, a normal scriptwriting video gets around 2,000 views. If I post one and it gets 2,000, that's fine. It did its job.")
para("But when ChatGPT 5 came out, I made a video on it and expected about 5,000 views, because the topic was much broader. After four weeks it had about 1,800. So I had to work out what went wrong, and the options are always the same: the title, the thumbnail, the script or the idea itself.")
img('gpt5_card.jpg', 4.0, caption='(The screenshot I put in my own notes: 1,800 views after 4 weeks.)')
para("In that case it was the timing. The GPT-5 hype lasted about two days, and my editors weren't ready for the video, so we posted it late. The idea was fine. We just showed up after everyone had stopped caring.")
img('chart_gpt5_expectation.jpg', 6.0, caption='(The video sits at about 3,100 views today, per Nexlev on 29 October 2026. Still well under what I expected.)')
h2('2. How Many People Are Still Watching At 30 Seconds')
para("On the retention graph, the only part I really study is the first 30 seconds. It shows you how strong your hook is. Everything after that matters too, but if half the room leaves in the first 30 seconds, nothing later in the video can save it.")
para("I've also found little to no connection between a higher average view duration and more views. A great average view duration doesn't stop a video from flopping, so I don't stare at it.")
para("**Try this:** open your last 10 videos and write two things next to each one: the views at day 30 and the percentage still watching at 30 seconds. That little table tells you more than an hour of clicking around Studio.")

# ================= GLOSSARY =================
h1('Words You Need To Know')
para("You'll see these words a lot in YouTube Studio. Read this once and the rest of the guide gets much easier.")
table([['Word', 'What it means'],
       ['Impressions', 'How many times YouTube showed your thumbnail to someone, on the homepage, in search or next to another video.'],
       ['Click-through rate (CTR)', 'Out of everyone who saw your thumbnail, the percentage who clicked it.'],
       ['Views and engaged views', 'Since 27 August 2026, a view counts as soon as the video starts playing. Engaged views only count people who actually stayed.'],
       ['Average view duration (AVD)', 'How long the average viewer watched, in minutes and seconds.'],
       ['Average percentage viewed', 'The same thing as a percentage of the video. 5 minutes of a 10-minute video is 50%.'],
       ['Retention graph', 'A line showing what percentage of people are still watching at each second of the video.'],
       ['Watch time', 'All the minutes everyone spent watching, added up.'],
       ['Traffic sources', 'Where your views came from: the homepage (browse), YouTube search, suggested videos, outside links and so on.'],
       ['Returning viewers', 'People who have watched your channel before and came back.'],
       ['RPM', 'What you earn from ads per 1,000 views, after YouTube takes its cut.']],
      [1.9, 4.6])
para("One note on views. Your CTR, average view duration, watch time and ad money all run on engaged views. So when I talk about views in this guide, I mean the real ones. I covered the August 2026 change in detail in my ALGORITHM guide.")

# ================= AVERAGES =================
h1('Before You Look At Anything, Find Your Own Averages')
para("People ask me all the time what a good click-through rate is. The only baseline that means anything is your own channel's click-through rate. If you haven't posted anything yet, I use 5% as the starting point. Once you have 10 videos, throw that number out and use yours.")
para("The catch is that your CTR changes with the age of the video. It's high in the first day, when YouTube mostly shows the video to people who already know you, and it drops as the video reaches strangers. So you need three averages, and this is how I get them.")
img('avg_ctr_steps.jpg', 6.0, caption='(From the analytics part of my 3-hour Claude course.)')
bullets(["Open the analytics for each of your last 10 videos.",
         "For each one, write down the CTR at 24 hours, at 7 days and at 30 days. In the Reach tab, change the date range at the top to match.",
         "Average each column on its own."], numbered=True)
para("For example, if your 24-hour average is 14%, your 7-day average is 9% and your 30-day average is 7%, those are your benchmarks. A new video at 10% after one day is behind. The same 10% at day 30 is ahead of normal.")
img('chart_ctr_benchmarks.jpg', 5.8, caption='(The example numbers I use in the course. Yours will be different, which is the whole point.)')
img('studio_impressions_ctr.jpg', 6.0, caption='(The Reach tab: impressions on the left, impressions click-through rate next to it.)')
para("Do the same for views. Sort your last 10 to 20 videos, find the middle one, and that's your normal. Anything above 3 times that number is a win worth studying. My own channel is below as an example.")
img('chart_my_last_30.jpg', 6.3, caption='(My last 30 long-form videos, from Nexlev on 29 October 2026. The blue bars are the outliers I study.)')
para("**Try this:** make a simple sheet with your last 10 videos and five columns: 24-hour CTR, 7-day CTR, 30-day CTR, views at day 30 and still watching at 30 seconds. Average each column. Every check in the rest of this guide compares a new video against that bottom row.")

# ================= 24 HOURS =================
h1('The First 24 Hours: What I Check')
para("In the first day I'm only asking one question: did the packaging work on the people YouTube showed it to first? Those people are mostly your subscribers and past viewers, so the numbers will look better than they really are. That's fine as long as you compare them against your own 24-hour average.")
h2('Step 1. Compare The CTR To Your 24-Hour Average')
para("If the CTR is below your 24-hour average, test a new thumbnail. If it's above, leave it alone. That's the whole rule.")
img('check_24h.jpg', 6.0, caption='(My 24-hour rule. The pie chart is a Databox survey of creators showing that most channels sit between 2% and 5%.)')
para("At Viral Bangers we go one step further on new uploads. Before the video goes live, the team designs 5 or 6 thumbnails and picks the one we think is best. Then we start an hourly test straight away with 4 or 5 of them, one hour each, during the hours our audience is most active. If one is clearly winning after the first full cycle, we stop the test and set it.")
img('new_upload_strategy.jpg', 6.0, caption='(How we test thumbnails on a brand new upload.)')
para("One thing to watch with hourly tests: the first thumbnail in the rotation gets a bump from subscriber notifications. So judge the test on CTR and average view duration, never on which version got the most views.")
h2('Step 2. Look At The First 30 Seconds')
para("Open the Engagement tab and look at the start of the retention graph. On the videos where I've used my best hooks, I usually get 60 to 70% of people still watching at 30 seconds. If 60% of people have already clicked off by then, the hook is weak and that's the first thing I'd fix on the next video.")
h2("Step 3. Don't Panic About Low Impressions")
para("Sometimes a video just sits there on day one. Usually YouTube feeds a new video around 1,000 impressions and then watches what people do with it. I had a creator I was coaching ask me why his video was dead, and it didn't even have 1,000 impressions yet. You can't learn anything from 800 impressions. Give it time, because impressions often come in steps, and a good video gets a bigger bump each time.")
para("**Try this:** next time you post, set a reminder for 24 hours later. Check two numbers only, the CTR and the percentage still watching at 30 seconds, and compare both to your sheet. If the CTR is under your average, swap the thumbnail. Don't touch anything else.")

# ================= 7 DAYS =================
h1('Day 7: Is YouTube Showing It To Strangers?')
para("By day 7 the video has usually left your existing audience. This is where most people panic, because the numbers go down. Most of the time, that drop is normal.")
h2('A Falling CTR Is Usually Normal')
para("When a video starts going out to a colder audience, CTR and retention are bound to go down. Strangers don't know who you are and don't trust you yet, and they have a shorter attention span for you than your fans do. So a lower CTR doesn't mean the thumbnail is bad.")
para("I saw this on a brand new channel we were growing from scratch. One video had a 4.6% CTR in its first day. Three days later it was at 1.5%, with the exact same thumbnail. That's normal, especially on a newer channel. YouTube showed it to our audience first, and then to people who had never heard of us.")
img('chart_ctr_drop.jpg', 5.8, caption='(Same video, same thumbnail, three days apart.)')
para("I said this on a call with Subscribr members at the time, and I still think it: don't worry about the analytics too much as long as you have a good title and thumbnail. I only start testing a new thumbnail once the video completely flatlines.")
h2('Step 1. Compare The CTR To Your 7-Day Average')
para("If it's below your 7-day average, test another thumbnail and let the test run for 7 to 14 days, then pick the winner. If it's above, don't touch it. Changing a thumbnail that's working can kill a video's momentum.")
img('check_7day.jpg', 6.0, caption='(My 7-day rule.)')
h2('Step 2. Check The CTR From Strangers Only')
para("The overall CTR mixes your fans and strangers together, and your fans click almost anything you post. If 1,000 subscribers all click a video because they know you, the CTR looks great even if no new viewer ever clicks it. So when I'm trying to get a video to spread, I filter the CTR by traffic source.")
bullets(["Open the video's analytics and go to the Reach tab.",
         "Click into the impressions click-through rate chart.",
         "Filter by traffic source and note the CTR from Browse features (the homepage) and Suggested videos.",
         "Those two are mostly strangers. If you test a new thumbnail, that's the CTR to watch."], numbered=True)
h2('Step 3. Read Your Traffic Sources')
para("The traffic sources box tells you how people found the video. Browse features means the homepage, where you're competing with MrBeast and Alex Hormozi. Suggested videos means YouTube recommended you next to or after another video. YouTube search means someone typed something in.")
img('studio_traffic_sources.jpg', 4.5, caption='(The "How viewers find this video" box in YouTube Studio.)')
para("I went through this with Tristan on my channel. He makes videos about SMS and iMessage for businesses, and his channel brings in about $300,000 a year. His YouTube search was doing really well at 33%, but browse was only 6%. That told us his videos were built to rank in search and almost never got picked up on the homepage, which is fine for buyers but caps how far a video can travel.")
img('tristan_traffic_sources.jpg', 5.0, caption='(Tristan\'s traffic sources: search at 33.2%, browse features at 6.4%.)')
img('bryan_tristan.jpg', 5.5, caption='(Going through Tristan\'s analytics in "Building a $1,000,000 YouTube Business For A Stranger in 40 Minutes".)')
para("**Try this:** open the video you posted last week, filter CTR by traffic source, and compare the browse CTR to the overall CTR. If browse is far lower, strangers aren't clicking. That's a thumbnail and title problem, and it's worth one test.")

# ================= 30 DAYS =================
h1('Day 30: This Is When I Judge The Video')
para("Now the video gets its real grade: views at day 30 against what you expected from that idea. Write the expectation down before you post, so you can't fool yourself afterwards.")
h2('If It Missed, Find Out Which Part Failed')
para("Go through the same list every time: the title, the thumbnail, the script and the idea. Check the timing too. My GPT-5 video had a good idea and a decent package, but it showed up after the hype was gone.")
h2('Now It\'s Time To Test The Title')
para("If the 30-day CTR is below your 30-day average, this is when I test the title. By now you've already tried the thumbnails at day 1 and day 7, so the title is the next thing to try. Change one thing at a time, so you know what made the difference.")
img('check_30day.jpg', 6.0, caption='(My 30-day rule.)')
h2('Long Videos Keep Growing After Day 30')
para("On videos of 30 minutes or longer, people often watch for a bit, go eat lunch, and come back to finish it a day later. So the average view duration can creep up over a month or two, from something like 6 minutes to 7 to 8. Most people never notice that, and they write off a long video too early.")
para("Views keep moving too. My GPT-5 video had about 1,800 views at four weeks and has about 3,100 today, so a video you wrote off can keep adding views for months.")
para("**Try this:** put a recurring 30-minute slot in your calendar once a month. Go through every video that turned 30 days old since the last one, write views against expectation, and next to each miss write which of the four parts you think failed.")
para("If you'd rather have a team doing this every week for your channel, from the ideas to the thumbnails to the tracking, that's what we do at Viral Bangers. You can book a call here: [[viralbangers.com/book|https://www.viralbangers.com/book]].")

# ================= RETENTION =================
h1('How To Read A Retention Graph')
para("The retention graph shows what percentage of people are still watching at every second of the video. Find it in the video's analytics under the Engagement tab. The shape tells you more than the average does.")
img('studio_retention_graph.jpg', 6.0, caption='(A retention graph in YouTube Studio: 7:19 average view duration, 40.8% average percentage viewed, on a 17:57 video.)')
h2('The Six Shapes You\'ll See')
img('chart_retention_shapes.jpg', 6.5, caption='(Drawings of the common shapes, so you can recognise them.)')
table([['Shape', 'What it usually means', 'What I change'],
       ['Small drop, then flat', 'The hook did its job and the video held up.', 'Nothing. Study it and make more like it.'],
       ['Half gone in 30 seconds', 'The opening didn\'t match the thumbnail and title, or it took too long to start.', 'Rewrite the hook so the first line confirms the click.'],
       ['Staircase', 'People leave after each point because they feel they got enough.', 'Tease what\'s coming next before you finish each point.'],
       ['Cliff near the end', 'A recap or a goodbye told people the video was over.', 'Cut the recap and end on your best moment.'],
       ['Spike', 'People rewound to watch something again.', 'Do more of whatever happened there.'],
       ['Slow slide all the way', 'The middle drags.', 'Cut filler and add story beats.']],
      [1.6, 2.6, 2.3])
para("I call that staircase segmentation loss. It happens a lot on list videos, where every finished point feels like a natural place to leave. And the recap cliff is one of the biggest retention killers I see. If a viewer needs a recap, they'll rewatch, and that rewatch is extra watch time for you. A recap just tells them they can click off now.")
img('retention_recap_dip.jpg', 5.5, caption='(From my retention video: the big dip near the end comes right where the recap starts.)')
img('retention_slow_decline.jpg', 5.5, caption='(A healthy shape: a drop at the start, then a long, slow decline.)')
h2('What Good Looks Like At 30 Seconds')
para("My own target is 60 to 70% still watching at 30 seconds. Other creators use similar numbers. These are theirs, so I've put their names next to them:")
table([['Who', 'What they say about 30-second retention'],
       ['Think Media', 'Typical videos range from about 48% (weak) to about 75% (strong).'],
       ['Linden Chasteen', 'Aim for 70%. Lower usually means the opening doesn\'t match the packaging.'],
       ['Jake Bryant', 'Around 75% is common for high-performing videos, and 90% or more is top tier.'],
       ['Marcus Jones', 'If 65 to 80% are gone by 30 seconds, the intro needs work.']],
      [1.8, 4.7])
h2('Use The Graph To Place Your Call To Action')
para("Where I like to pitch is at my average view duration. Tristan's average view duration was about 2 minutes, but he always pitched at the end of the video. So I told him to pitch a lead magnet at the 2-minute mark instead.")
img('tristan_ctr_avd.jpg', 5.5, caption='(Tristan\'s Reach tab: 5.4% CTR, and the 2-minute average view duration I circled.)')
para("**Try this:** open your three best and three worst videos and screenshot the first minute of each retention graph. Put them side by side and watch the first 30 seconds of each video. The difference between the two groups is usually obvious within a few minutes.")

# ================= AVD =================
h1('Average View Duration, Percentage Viewed And Watch Time')
para("These three get mixed up a lot. Average view duration is minutes. Average percentage viewed is the share of the video. Watch time is all the minutes added together.")
img('studio_watch_time.jpg', 6.0, caption='(Watch time in hours, with the average view duration next to it.)')
para("A lower percentage isn't automatically worse. A 10-minute video watched for 5 minutes gives you more watch time than a 3-minute video watched for 2 minutes, even though the percentage looks worse. YouTube counts the minutes, so I don't panic when a longer video has a lower percentage.")
img('chart_watch_time_math.jpg', 5.8, caption='(Same idea in a picture.)')
para("Watch out for one trap. A small, loyal audience can make a video's average view duration look amazing. Marcus Jones points out that a personal story video on a small channel often gets great retention, because only your fans click it, and then it goes nowhere because strangers don't care. So I always read average view duration next to the views.")
para("And look at the device type report (Advanced mode, then Device type). Oscar Owen showed a 1 million subscriber channel where viewers on a TV watched for 2 minutes 48 seconds on average and phone viewers for 1 minute 27 seconds. My own rule is simple: shorter for mobile, longer for TV viewers.")
para("**Try this:** in Advanced mode, add the Device type report and check what share of your watch time comes from TV. If it's big, your audience is happy to sit through longer videos.")

# ================= RETURNING =================
h1('Returning Viewers Matter More Than Subscribers')
para("Subscribers don't mean much anymore. There are channels with millions of subscribers that can barely get a thousand views on a video. Returning viewers are your only real asset, because that's how you build an audience. When I want to know how a channel is really doing, I want to see returning viewers going up month to month.")
para("Find it in the Audience tab. YouTube now splits your viewers into new, casual and regular viewers, so you can see how many people keep coming back.")
para("The fastest way I know to burn returning viewers is to pitch your product in every single video. Tristan was doing that, with the same \"click the link below\" every time. Someone who comes back every week gets tired of being sold to. Give them a reason to come back, like a useful free guide, and save the hard pitch for the right videos.")
para("This is also why session time matters so much for a business. When someone watches three of your videos in a row, they start to trust you, and if you sell a service, coaching or software, people who trust you are a lot more likely to give you money. One viewer watching three of your videos beats three viewers watching one video each.")
para("**Try this:** open the Audience tab, set the range to the last 90 days, and write down your returning viewers. Do it again next month. That one number tells you more about your channel than your subscriber count.")

# ================= WHO IS WATCHING =================
h1('Check Who Is Actually Watching')
para("Views from the wrong people can hurt you. The most important thing on YouTube is your audience. If you build the wrong one, you'll be serving people who won't pay you for a long time.")
para("Tristan had a Short with almost 3 million views. It looked great, but a lot of those views came from paid ads someone ran, and the top countries were India at 57.2%, then Morocco, Algeria, Bangladesh and Saudi Arabia. His buyers are businesses using tools like GoHighLevel and HubSpot, so that just wasn't his audience. I told him to unlist it.")
img('tristan_short_3m.jpg', 5.5, caption='(Tristan\'s Short: 2,986,753 views.)')
img('tristan_geography.jpg', 3.8, caption='(Where those views came from.)')
para("He said it hurt his ego, and I get that. But when the wrong people pile into your audience, your click-through rate slowly drops, because YouTube keeps showing your new videos to people who were never going to click them. You won't feel it much at 1,900 subscribers. You will at 20,000.")
para("This is also why I filter my own analytics to long-form views only. Nobody watches a long video about a piece of software unless they're thinking about buying it. A Short is something people scroll past while competing with food creators and brain rot, so the intent is much lower.")
para("**Try this:** open your top 5 videos by views, one at a time, and check the Audience tab for each: countries and age. If any of them pulled in people who could never buy from you, think about unlisting it.")

# ================= TESTING =================
h1('When I Change A Thumbnail Or Title')
para("A/B testing is great for reviving a flatlined video, and for pushing a video that's already doing well even further. But if you do it wrong, you can kill a video's growth. So I follow a few rules.")
img('testing_rules.jpg', 6.0, caption='(My testing rules, from the Claude course.)')
bullets(["Only test when a video is below your average for its age (24 hours, 7 days or 30 days). If it's above, leave it alone.",
         "Test with cold traffic. If only your subscribers see the test, the results are skewed, because they already like you.",
         "Test big changes, like a completely different idea or angle. Small tweaks like a different shirt colour aren't worth a test.",
         "Test one thing at a time. Thumbnail first, then the title. Swapping both at once usually means you learn nothing."], numbered=True)
para("YouTube's own Test & Compare tool is fine for most people. You'll find it in the thumbnail section when you edit a video. It picks the winner by watch time share, which is a good sign, because it rewards the thumbnail that gets people to stay as well as click.")
img('test_compare_report.jpg', 5.5, caption='(A Test & Compare report. The winning thumbnail got 59.7% of the watch time.)')
para("If you want to go further, our team uses thumbnailtest.com. It tests as many versions as you like, can rotate every hour on a new upload, and scores each one on CTR multiplied by average view duration. For example, a 6.07% CTR and a 369-second average view duration gives a score of 22,398. That multiplication matters, because a clickbait thumbnail can win on CTR and still lose once people leave in the first minute.")
para("For older videos we test daily for about two weeks and always keep the original in the test, so we know whether the new version actually beats it. We rework old videos that underperformed, top videos that could do even better, and any thumbnail that shows an old year, an old tool or an old version of the creator.")
para("**Try this:** pick one video from the last 90 days that's below your 30-day CTR average. Make one new thumbnail with a completely different idea, run Test & Compare for 14 days, and keep whichever gets more watch time share.")

# ================= DIAGNOSIS =================
h1('How I Diagnose A Video (If X Is Low And Y Is High)')
para("When a video misses, I compare its CTR and its 30-second retention against my own averages. Those two numbers together usually point at the problem.")
img('chart_diagnosis.jpg', 5.5, caption='(The four combinations I see most.)')
table([['If this is low', 'And this is high', 'The problem is usually', 'What I do'],
       ['CTR', 'Retention at 30 seconds', 'The package. People who click like it, too few click.', 'New thumbnail first, then the title.'],
       ['Retention at 30 seconds', 'CTR', 'The hook doesn\'t deliver what the package promised.', 'Rewrite the opening so the first line confirms the click.'],
       ['Views', 'CTR and retention', 'Not enough impressions yet, or the topic is small.', 'Wait for 1,000+ impressions. If it flatlines, test the package.'],
       ['Impressions', 'Nothing yet', 'YouTube hasn\'t tested it, or nobody wants this topic.', 'Give it time. If it never gets going, pick bigger ideas.'],
       ['Browse CTR', 'Search traffic', 'Built to rank, but not clickable on the homepage.', 'Test a thumbnail aimed at strangers.'],
       ['Views at day 30', 'Your expectation', 'One of title, thumbnail, script, idea or timing.', 'Write down which one, and don\'t repeat it.'],
       ['Leads or calls', 'Views', 'Wrong audience, or no clear ask.', 'Ask once, clearly, before most people leave.']],
      [1.35, 1.35, 2.05, 1.75])
para("I've seen both of these on real channels. A creator I was coaching had 75% still watching at 30 seconds and 40% still there at the 10-minute mark, and then the views went flat overnight. With retention that good, the content clearly worked, so it was a package problem. Another one had a 6.4% CTR and about 5 minutes of average view duration on top-10 style videos, and still got stuck around 25,000 views. His script was fine, so we focused on better ideas and posting twice a week to test more of them.")
para("**Try this:** take your worst video from the last three months and fill in one row of the table above for it. Write the fix on a sticky note and apply it to your next video.")

# ================= MONEY =================
h1('The Numbers That Actually Pay You')
para("If you sell something, this is the most important section. I measure YouTube in booked calls and revenue, because monetization is way more important than growing your channel. If it doesn't make you money, it's very hard to justify making the videos.")
para("The tracking we run for clients follows each sale back to the exact video that started it. Across 207 channels, 26,621 videos and over 336 million views, it has traced more than $35 million in sales. And views barely predicted the money. Link clicks were over 4 times better at predicting it, and the 100 most viewed videos made only about 11% of it.")
img('chart_link_clicks_money.jpg', 6.3, caption='(Videos where 0.5 to 1% of viewers clicked a link made about 40 times more per video.)')
h2('The Business Numbers I Track For Every Video')
table([['Number', 'How to get it'],
       ['Link clicks', 'Use a different tracking link in each video\'s description, so you can see which video sent each click.'],
       ['Link-click rate', 'Link clicks divided by views. Under 0.25% means people aren\'t being asked clearly.'],
       ['Leads', 'Opt-ins or form fills from that link.'],
       ['Booked calls', 'Ask on your booking form which video they watched, and check the tracking link.'],
       ['Sales and cash collected', 'Match each sale back to the video. Add it to the same sheet.']],
      [1.9, 4.6])
h2('What That Looks Like In Real Life')
para("Clover Trading's video \"9 Years of Trading Experience in 31 Minutes\" got about 17,000 views and booked 30 calls. But a strategy video with only 8,000 views made more money than both of the other videos we were testing at the time. Only about 28% of their viewers made it to the end of a 30-minute video, so we added a 15-second call to action at minute 3. Link clicks went up 20% and conversions went up 25%.")
para("Scott Taylor's backtest videos only got 3,000 to 4,000 views each, but the first few booked about 7 calls between them. And my own first video got about 3,500 views in 5 days and booked 4 calls. On a normal analytics screen, all of those look small.")
para("Shane Hummus uses a number I like for this: qualified booked calls per 1,000 views. In his example, a format that gets 10,000 views and 1 call per 1,000 views books 10 calls. A format with 4,000 views and 3 calls per 1,000 books 12. The smaller one wins.")
para("**Try this:** put a separate tracking link in the descriptions of your next 5 videos and add a question to your booking form: \"Which video made you book this call?\" After a month, rank your videos by calls instead of views. The order usually surprises people.")

# ================= BUSINESS OWNER =================
h1('How To Use This If You Run A Business')
para("You don't have time to live in YouTube Studio, and you don't need to. This is the routine I'd give a business owner.")
table([['When', 'What to check', 'Time'],
       ['24 hours after posting', 'CTR against your 24-hour average, and still watching at 30 seconds. Swap the thumbnail if CTR is low.', '5 minutes'],
       ['Day 7', 'CTR against your 7-day average, browse CTR, traffic sources.', '5 minutes'],
       ['Day 30', 'Views against expectation, then the title if CTR is low.', '5 minutes'],
       ['Every week', 'Link clicks, leads and booked calls by video.', '10 minutes'],
       ['Every month', 'Your review: which ideas and hooks worked, returning viewers, who is watching.', '30 minutes']],
      [1.7, 3.6, 1.2])
h2('My Monthly Review')
para("Once a month I sit down and review my videos. I want to know which ideas worked and which hooks worked, so the next month's videos copy the winners.")
para("I'm careful with comments. The comment section is often more noise than signal, because someone who isn't your ideal customer can comment something and you'll think it's what your buyers want. Tristan noticed this on his own channel, where the comments still came from his old audience. For feedback I'd much rather ask a few friends who make YouTube videos. They're more likely to know what's good and what isn't.")
para("Oscar Owen deleted the YouTube Studio app from his phone so he'd stop checking his numbers all day, and I think that's smart for most business owners. The checks in this guide are all you need.")
para("**Try this:** this week, block three short slots in your calendar: one for 24 hours after your next upload, one for day 7 and one for day 30. Put the checks from the table above in each calendar note so you don't have to think about it.")

# ================= CHECKLIST =================
h1('The Checklist')
para("Run every video through this:")
checklist(["I know my channel's average CTR at 24 hours, 7 days and 30 days (from my last 10 videos)",
           "I know my normal views (the middle video of my last 10 to 20)",
           "I wrote down how many views I expect before I posted",
           "24 hours: CTR compared to my 24-hour average, thumbnail swapped if it's below",
           "24 hours: checked how many people are still watching at 30 seconds",
           "I didn't judge the video before it had at least 1,000 impressions",
           "Day 7: CTR compared to my 7-day average, checked CTR from browse and suggested only",
           "Day 7: checked traffic sources and where the views came from",
           "Day 30: views compared to what I expected, and I wrote down which part missed",
           "Day 30: tested the title only if the 30-day CTR is below average",
           "I tested one thing at a time, and made it a big change",
           "I checked the retention graph for a staircase or an end-of-video cliff",
           "My call to action comes around my average view duration",
           "I checked the countries and ages of my top videos",
           "Returning viewers are written down, and I compare them month to month",
           "Every video has its own tracking link, and I count link clicks, leads and calls",
           "Once a month I review which ideas and hooks worked"])

# ================= CTA =================
h1('Want Us To Do This For You?')
para("This is what we do at Viral Bangers every week. We find the ideas, write the scripts, edit the videos and test the thumbnails, and then we track which videos turn into booked calls so the next ones get better. All you have to do is show up and record.")
para("**Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]")
