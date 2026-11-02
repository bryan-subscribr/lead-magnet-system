# STUDIO lead magnet: "The Hidden YouTube Studio Tabs Guide". Voice: Bryan Ng. Images in ./img (real Studio frames, sources in work/RESEARCH.md).

title_page('The Hidden YouTube Studio Tabs Guide',
           [('The Free Tabs That Show You ', False), ('Exactly', True), (' What To Make Next', False)], hero='hero.jpg')
toc_page(levels=1)

# ================= TL;DR =================
h1('TL;DR')
para("Most people open YouTube Studio to check one number: views. I was the same. Back when I couldn't get a video past 1,000 views, I opened Studio \"like the junkie I am\" and saw one video sitting at 11,000 views, 10 times my average. After that I noticed the videos I put the most prep into tended to do better.")
para("The prep is the part this guide is about. Inside Studio there are a few free tabs that tell you what your viewers search for and which other channels they watch. Most creators never scroll past the first screen, so they never see them.")
para("These are the six places I'll walk you through, with real screenshots of each one:")
bullets(["Trends (it used to be called Research): the searches your audience types, and the ones with no good video yet.",
         "Audience: the other channels and videos your viewers watched this week and this month.",
         "Reach, inside each video: the exact search terms and the videos that sent people to you.",
         "Inspiration: YouTube's own AI idea board, built from your audience data.",
         "Advanced mode: one table to compare every video you've made.",
         "A/B testing: up to three titles or thumbnails tested on real viewers."], numbered=True)
para("Every section has where to click, what you're looking at, a worked example, and a \"Try this\" step. Give it 20 minutes a week and you'll stop guessing what to film. If you sell a service, there's a full section near the end on using these tabs to find the exact questions your buyers type into YouTube.")

# ================= WHO WE ARE =================
h1('Who We Are')
para("My name is Bryan, and I run Viral Bangers with my co-founder Mauricio. We're a YouTube agency for business owners who sell something, like consultants, coaches, traders and info product businesses. We handle the ideas, scripts, editing and thumbnails, so all you do is show up and record. One of the creators we work with is Brad Goh (The Trading Geek), who has over 1.8 million subscribers on YouTube.")
para("A few of the people we've worked with:")
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

# ================= LOOKS DIFFERENT =================
h1('Why Your Studio Might Look Different From Mine')
para("A quick warning before we start: YouTube changed the names of these tabs during 2026, and it rolls changes out to different channels at different times. ShortPrompt's walkthrough from this month says the layout \"can vary depending on your account, country, language, or device\". So if a button I mention isn't in the exact spot, look one tab over.")
para("Right now most channels see four tabs at the top of Analytics: Overview, Content, Audience and Trends. There's also an Advanced mode button in the top right corner.")
img('analytics_tabs_light.jpg', 6.5, caption='(Channel analytics in 2026: Overview, Content, Audience, Trends, plus Advanced mode. From Jeremiah Tutorials.)')
para("Two years ago the fourth tab was called Research. You'll still see that name in a lot of older tutorials, and it's the same idea: what people search for on YouTube.")
img('analytics_tabs_2024_research.jpg', 6.0, caption='(The same row in early 2024, when the last tab was still "Research". From Nate Black.)')
para("And it's changing again. At Made On YouTube a month ago, YouTube announced that Analytics is being upgraded to \"Insights\", with a new Research area inside it. I cover that at the end. Some channels already see it.")
img('insights_new_home.jpg', 6.5, caption='(The new Insights page YouTube showed at Made On YouTube, with Content, Audience, Revenue and Research tabs. From Creator Insider.)')
para("Also, several of these reports need some viewers before they fill in. Make Money Matt and Think Media both point out that very small or brand new channels often see \"not enough data\" in the Audience tab. If that's you, the Trends tab still works, because it can look at searches across all of YouTube, including people who don't watch you yet.")

# ================= MAP =================
h1('Where To Click: The Whole Map')
para("Every report in this guide, in one place. Desktop Studio shows the most; the mobile app shows less.")
table([['Report', 'Where to click', 'What it tells you'],
       ['What people are looking for', 'Analytics > Trends', 'Top searches from your audience'],
       ['Topic page + Saved', 'Analytics > Trends > search a topic', 'Searches and popular videos for one topic, with a heart to save'],
       ['Content gap', 'Shown as a label on a search (when YouTube flags one)', 'People search it, but the results are thin, old or poor'],
       ['Channels your audience watches', 'Analytics > Audience (scroll)', 'Channels your viewers kept going back to, last 28 days'],
       ['What your audience watches', 'Analytics > Audience (scroll)', 'Other videos they watched, last 7 days'],
       ['Formats your viewers watch', 'Analytics > Audience (scroll)', 'Long videos vs Shorts vs live'],
       ['When your viewers are on YouTube', 'Analytics > Audience (scroll)', 'Days and hours your viewers are online'],
       ['YouTube search terms', 'Content > a video > Analytics > Reach', 'Exact words people typed to find that video'],
       ['Content suggesting this video', 'Content > a video > Analytics > Reach', 'Which videos YouTube showed yours next to'],
       ['Inspiration', 'Content > Inspiration', 'AI ideas, titles, outlines and thumbnails'],
       ['Advanced mode', 'Analytics > Advanced mode (top right)', 'All your videos in one table, with filters'],
       ['A/B testing', 'Content > a video > Details > icon under title or thumbnail', 'Tests up to 3 titles or thumbnails']],
      [1.7, 2.3, 2.5], bold_rows=(0,))

# ================= TRENDS =================
h1('Tab 1: Trends, Where Your Viewers Tell You What To Make')
para("This is the tab I'd open first. It shows what people are searching for on YouTube, filtered toward the people who watch you.")
h2('Where to click')
para("**Step 1.** Open YouTube Studio on a computer and click Analytics in the left menu.")
para("**Step 2.** Click Trends in the row of tabs at the top. On some accounts it still says Research.")
img('trends_get_ideas.jpg', 6.5, caption='(The Trends tab. A search box, a Saved list, and a few starter ideas. From Jeremiah Tutorials.)')
para("You'll notice a grey bar at the top: \"AI tools for brainstorming video ideas have moved to Inspiration.\" That's YouTube telling you the AI part now lives in its own tab, which I cover in Tab 4.")
h2('What it shows')
para("On a channel with some history, the first card is \"What people are looking for\". Sprizzy's breakdown describes it as top searches based on your audience over the last four weeks. Click Show all to see the full list.")
img('trends_what_people_look_for.jpg', 6.5, caption='(\"What people are looking for\" on a YouTube-news channel. Every box is a search their viewers typed. From YT UNLOCKED.)')
para("Below that is \"New videos to inspire you\". These are recent videos, from other channels, that your type of viewer is watching right now.")
img('trends_new_videos_inspire.jpg', 6.5, caption='(\"New videos to inspire you\" on the same channel. From YT UNLOCKED.)')
img('trends_tea_2026.jpg', 6.0, caption='(The same two cards on a small tech channel this month. From Tea Break Tutorials.)')
h2('How to read a topic page')
para("Type a topic into the search box and you get a page just for that topic. It shows \"Top searches for this topic\", each with a volume label like Medium volume, and \"What people are watching\", which are the popular videos for it.")
img('trends_topic_page.jpg', 6.5, caption='(A topic page for \"easy and fast fluffy pancakes recipe\". Three real searches, then the videos people watch for them. From Jeremiah Tutorials.)')
para("Click the heart next to any search to save it. Your saved searches build a list you can come back to, and the counter next to Saved goes up.")
img('trends_saved_hearts.jpg', 6.5, caption='(Saving searches with the heart icon. YouTube confirms with \"Saved. You\'ll see similar topics on your feed.\" From Jeremiah Tutorials.)')
para("Read the volume labels as rough. Marcus Jones found YouTube's own tool saying \"not many search results\" for a phrase that does get searched, and Shane Hummus says to trust the gap between two numbers more than the numbers themselves. So compare a High against a Medium, and don't lean on the exact count.")
h2('What a content gap is')
para("Sometimes YouTube marks a search as a Content gap. In its own words, a content gap is when viewers can't find any results, can't find an exact match, or can't find relevant videos, \"for example, the content is old or low quality.\"")
img('research_old_content_gap_tooltip.jpg', 5.5, caption='(YouTube\'s own explanation of a content gap, from the older Research tab. From AndrewMurrayTV.)')
img('research_old_content_gap_labels.jpg', 5.5, caption='(Searches tagged \"Content Gap\" under each phrase. From AndrewMurrayTV.)')
para("Nate Curtiss calls these the first thing to check for topic ideas: lots of people searching, not much good content to watch. The 2026 tutorials add one fair warning. ShortPrompt calls a content gap \"an opportunity signal, not a promise of views.\" You still need a good video.")
para("In the 2026 Trends tab the content gap label shows up when YouTube spots one, and ShortPrompt notes it currently surfaces gaps for Shorts in particular. On older accounts you'll see the version below, with \"Searches across YouTube\", \"Your viewers' searches\" and \"Saved\".")
img('research_old_explore.jpg', 6.5, caption='(The old Research tab: \"Explore what viewers are searching for on YouTube\". From AndrewMurrayTV.)')
h2('Worked example')
para("Look at the YouTube-news channel in the screenshot above. Their viewers searched \"how views are counted in youtube\", \"update how we count public view\" and \"youtube new views policy\". That's three searches about one change. Instead of three videos, that's one video with a plain title, something like \"YouTube Changed How Views Are Counted (What It Means For Your Channel)\", and the three phrases go in the script and description.")
para("Think Media did the same thing with a fishing example. They typed \"bass fishing\" and saw \"fall bass fishing\" and \"October bass fishing\" come up, which tells you what to film and when to post it.")
para("**Try this:** Open Trends, click Show all on \"What people are looking for\", and heart every search you could answer better than the current videos. Stop at ten. Then search each one on YouTube and check if the top results are old, off topic or weak. The ones that are become your next ideas.")

# ================= AUDIENCE =================
h1('Tab 2: Audience, Who Else Your Viewers Watch')
para("If Trends tells you what people search, Audience tells you what they watch when they're not watching you. Think Media rates it as one of the most important tabs in Studio, and it's the one most people never scroll down far enough to find.")
h2('Where to click')
para("**Step 1.** Analytics, then the Audience tab at the top.")
para("**Step 2.** Scroll down past the first chart. The useful cards are lower on the page.")
h2('What it shows')
para("PexBell's 2026 walkthrough lists them like this, and the screenshots match:")
bullets(["Channels your audience watches: channels your viewers kept going back to in the last 28 days.",
         "What your audience watches: videos, Shorts, live streams and podcasts they watched elsewhere in the last 7 days.",
         "Formats your viewers watch: how much they watch long videos vs Shorts vs live, last 28 days.",
         "When your viewers are on YouTube: the days and hours they're online, last 28 days.",
         "Audience by watch behavior: new, casual and regular viewers."])
img('audience_channels_watch_dark.jpg', 6.0, caption='(\"Popular with different audiences\" and \"Channels your audience watches\", last 28 days. From YT UNLOCKED.)')
img('audience_what_they_watch_dark.jpg', 6.0, caption='(\"What your audience watches\", last 7 days, with \"Formats your viewers watch on YouTube\" underneath. From YT UNLOCKED.)')
para("The \"What your audience watches\" card is a rolling seven days. Sprizzy's tip is to read it every upload day, because the topic in it today will be gone by next week.")
para("There's a version of this for single videos too. Open any video's analytics, click Audience, and you'll see \"Viewers also watch\", the other videos people who watched that one went on to watch, over the last 90 days.")
img('video_viewers_also_watch.jpg', 6.5, caption='(Inside one video: \"Audience by watch behavior\" and \"Viewers also watch\". From Think Media.)')
img('audience_watch_behavior_tea.jpg', 5.5, caption='(\"Audience by watch behavior\" on a small channel: 99.5% new viewers, so almost nobody is coming back yet. From Tea Break Tutorials.)')
para("PexBell defines the groups this way: casual viewers watched at least once a month for one to five months of the past year, and regular viewers did it for more than six months. If almost everyone is new, people like single videos but aren't sticking around for your channel.")
h2('How to read it')
para("Make Money Matt's advice on the videos list is to make your own version of what's already working for your viewers. Sprizzy pushes it one step further, and I agree with this one: make the video they'd want next, the follow-up to what they just watched. If your viewers watched two \"budget lighting\" videos this week, a third budget lighting video competes with both. A video on \"where to put three lights in a one-room studio\" is the next question they'll have.")
para("Use the channels list to study people. Subscribr Academy's notes say to go through those channels and find their outliers, the videos with far more views than the channel usually gets. In one example a small channel's video about \"Canada's most important canal\" had 712,000 views, way over its usual numbers. That's a topic your viewers already proved they'll click.")
para("The schedule graph helps less than people think. A YouTube employee on Think Media says it's mostly context: if you post at a peak time and the video still flops, the problem is more likely the title or thumbnail. Linden Chasteen's rule if you want one: post at the last faded bar before the bright ones start.")
h2('Worked example')
para("Look at the screenshot again. That channel's viewers watched Technical Yogi (2.1 million subscribers) and Creators Income Academy (72,700) this month, and the videos list shows a YouTube update from Technical Yogi with 74,600 views in 5 days. So this week the follow-up video is about that same update, from their own angle. This month, the channels list gives them five creators to study and pitch a collab to.")
para("**Try this:** Scroll to \"What your audience watches\" and write down the three titles that come up most. For each one, write the question a viewer would have after watching it. That question is your title. Then open the top three channels in \"Channels your audience watches\", sort by Popular, and note any video doing 5 to 10 times their normal views.")

# ================= REACH =================
h1('Tab 3: Reach, The Exact Words People Typed To Find You')
para("The first two tabs are channel-wide. This one is inside each video, and it's where you see what actually brought people in.")
h2('Where to click')
para("**Step 1.** Click Content in the left menu, hover over a video, and click the Analytics icon.")
para("**Step 2.** Click Reach at the top, then scroll down to the traffic source cards.")
img('reach_card_tea.jpg', 6.5, caption='(A video\'s Reach tab: \"How viewers find this video\" and \"Impressions and how they led to watch time\". From Tea Break Tutorials.)')
para("Small note on names: in 2026 YouTube calls these \"Thumbnail impressions\" and \"Thumbnail click-through rate\". An impression is one time your thumbnail was shown to someone. Click-through rate is the share of those people who clicked.")
img('reach_thumbnail_impressions.jpg', 5.5, caption='(2,600 thumbnail impressions (shown as 2.6k), 97.5% from YouTube recommending the video, and a 1.4% thumbnail click-through rate. From Tea Break Tutorials.)')
h2('YouTube search terms')
para("Scroll to the YouTube search terms card. These are the exact phrases people typed before they clicked your video. Make Money Matt says each query is a possible video idea, and Nate Black adds that it's most useful when search is a big chunk of that video's traffic.")
img('reach_search_terms_dark.jpg', 6.0, caption='(YouTube search terms for one video: \"youtube new update\" 37.7%, then \"youtube update\" and \"new youtube update\". From YT UNLOCKED.)')
h2('Suggested videos and content suggesting this video')
para("The other card to open is \"Content suggesting this video\". It lists the videos YouTube placed yours next to, or played after. On a channel-wide level you'll find the same list under Content, \"How viewers find your videos\", then Suggested videos.")
img('reach_content_suggesting.jpg', 6.0, caption='(\"Content suggesting this video\": the videos YouTube showed this one beside. From YT UNLOCKED.)')
img('reach_suggested_overview_dark.jpg', 6.0, caption='(Channel-wide \"How viewers find your videos\" with Suggested videos selected. 48.9% of this small channel\'s views came from suggestions. From Nate Black.)')
img('reach_suggested_table_dark.jpg', 6.5, caption='(The full suggested videos table, with impressions, click-through rate and views for each one. From Nate Black.)')
h2('How to read it')
para("Nate Black's check is simple. Go through the list of videos suggesting yours. If less than 70% of them are aimed at the audience you want, YouTube hasn't figured out who you're for yet. His fix is to say who the video is for out loud in the video, in the title and thumbnail, and in the first line of the description.")
para("Subscribr Academy's notes have a good example of this going wrong: a channel making writing advice found it was being suggested next to Star Wars commentary. Most of their views were coming from Star Wars fans.")
h2('Worked example')
para("In Nate Black's table, the top video sending people to him was one of his own, \"My SaaS User Growth System\", at 50% of suggested views. That's the healthy pattern Make Money Matt describes, where your own videos feed each other. When it's another creator's video at the top instead, Make Money Matt's advice is to make more videos close to that one in topic and style, so YouTube keeps putting you next to it.")
para("**Try this:** Open your three best videos from the last 90 days. In each one, copy the top five YouTube search terms and the top five videos in \"Content suggesting this video\" into a note. Any search term that shows up twice is a video on its own. Any outside channel that shows up twice goes on your study list.")

para("If you'd rather have someone run this research every week and turn it into scripts, that's what we do for our clients. **Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]")

# ================= INSPIRATION =================
h1('Tab 4: Inspiration, YouTube\'s Own Idea Generator')
para("Inspiration is the AI part of Studio. YouTube moved it out of the Research tab and into its own spot, which is why the Trends page now has that grey \"moved to Inspiration\" bar.")
h2('Where to click')
para("YouTube's own tutorial says: Studio on desktop, then the Content page, then Inspiration. It sits as a tab next to Videos and Shorts.")
img('inspiration_content_tab.jpg', 6.0, caption='(Content > Inspiration, from YouTube\'s official walkthrough. From YouTube Creators.)')
h2('What it shows')
para("Type a topic in the \"Let's brainstorm\" box and click Create ideas. Click any idea and you get a suggested outline, title ideas and thumbnail options, each of which you can rework with a prompt like \"make it shorter\". Hit Save to keep it.")
img('inspiration_brainstorm_box.jpg', 4.5, caption='(The \"Let\'s brainstorm\" box with suggestion chips. From YouTube Creators.)')
img('inspiration_idea_page.jpg', 6.0, caption='(One idea opened up: outline, titles and thumbnails, with a box to change it. From YouTube Creators.)')
img('inspiration_titles.jpg', 6.0, caption='(The titles screen. From YouTube Creators.)')
h2('How to read it')
para("The guy who built Studio told Aprilynne Alter where the ideas come from: high search volume where there may not be enough content, plus the other interests your audience has. Think Media adds that it can show a prediction of how likely a topic is to get views on your channel.")
para("Use it as a sparring partner. Think Media's YouTube employee interview says not to let it replace your own judgment, and to still test ideas it rates as low interest if you have a reason to believe in them. The titles it writes are generic, so treat them as a first draft.")
para("**Try this:** Take one search you saved in Trends and paste it into Inspiration. Read the outline it gives you and write down what's missing that only you know, like a story or a real number from your business. That gap between its outline and yours is what makes your video worth clicking.")

# ================= ADVANCED =================
h1('Tab 5: Advanced Mode, Every Video In One Table')
para("Think Media calls Advanced mode one of the \"hidden gems\" of YouTube, and I agree. It's a small button in the top right of Analytics.")
img('advanced_mode_button.jpg', 5.0, caption='(The Advanced mode button: \"Access groups, comparisons, filters and more customizable charts\". From Think Media.)')
h2('What it shows')
para("It opens a table of every video on your channel for whatever date range you pick, with views, watch time, subscribers and more. Click the plus sign to add a column, like average view duration or impressions click-through rate.")
img('advanced_mode_table.jpg', 6.5, caption='(Advanced mode on Think Media\'s channel: 12,138,412 views and 44,534 subscribers over 90 days, broken down by video. From Think Media.)')
para("The filter that matters most is content type. If you post Shorts and long videos, the numbers mix together. Filter to Videos and you see your long-form on its own.")
img('advanced_content_type_filter.jpg', 6.0, caption='(Filtering to long-form only with Content type > Videos. From Think Media.)')
para("Think Media also suggests exporting the table to Google Sheets and handing it to an AI tool with a question like \"what were my top 10 videos by click-through rate last month?\" That's a fast way to spot the topics worth a part two.")
para("**Try this:** Open Advanced mode, set the date to the last 365 days, filter to Videos, and sort by views. Write the top five and bottom five side by side. Look for what the top five share in topic or title shape. That's your pattern, and it's more reliable than any tip from me.")

# ================= AB =================
h1('Tab 6: A/B Testing, Let Viewers Pick Your Title')
para("Once Trends and Audience tell you what to make, A/B testing helps you package it. Older tutorials call it Test & Compare. YouTube now calls it A/B testing.")
h2('Where to click')
para("YouTube's official video says: open the video details page on Studio desktop, then click the icon under the title or thumbnail section. You can do it while publishing a new video or on one that's already live.")
img('ab_thumbnail_section.jpg', 5.5, caption='(The thumbnail section with Upload file, Auto-generated and A/B testing. From YouTube Creators.)')
img('ab_dialog.jpg', 5.5, caption='(Pick Title only, Thumbnail only, or Title and thumbnail, then Run test. From YouTube Creators.)')
h2('The rules, straight from YouTube')
bullets(["Up to three titles, three thumbnails, or three title and thumbnail pairs.",
         "Titles must be under 100 characters.",
         "Only public long-form videos. It won't run on made-for-kids, mature or live videos.",
         "YouTube picks the winner by watch time share.",
         "Results take anywhere from a few hours to a couple of weeks. The more different your options are, and the more impressions the video gets, the faster it finishes.",
         "If there's no clear winner, it says \"Performed same\" and keeps your first option.",
         "Starting a new test deletes the old one."])
img('ab_view_test_report.jpg', 5.5, caption='(Check progress any time with \"View test report\". From YouTube Creators.)')
img('ab_test_report.jpg', 5.5, caption='(A finished report: the first option won with 50% of watch time share. From YouTube Creators.)')
h2('How to read it')
para("Because it judges on watch time, a clickbait title that people leave fast will lose. Vireo Video points out that this is the big difference from older tools like TubeBuddy, which rotated every 24 hours and judged on click-through rate.")
para("Jake Thomas, talking to Jay Clouse, suggests waiting about five days after publishing before you test, because your most loyal subscribers click almost anything in the first day or two. YouTube itself suggests starting with a few older videos to learn what your audience likes.")
para("**Try this:** Pick one older video that got impressions but few clicks. Make two new thumbnails that are clearly different from the current one (say, a different face and different text) and run a thumbnail-only test. Write down what won and why you think it did.")

# ================= WHAT'S NEXT =================
h1('What YouTube Just Announced (Coming To Your Studio)')
para("At Made On YouTube a month ago, YouTube showed the next version of these tabs. Some channels have it already, most don't yet, so treat this as a preview.")
bullets(["Analytics becomes \"Insights\", with a new Research area that shows top-performing videos beyond your channel, tailored to your audience and niche. It flags outliers and summarises patterns across lots of videos.",
         "You can upload draft cuts of a video and get feedback before you publish, plus thumbnails generated right in the draft.",
         "A/B testing on the whole video. Upload two cuts with different hooks and YouTube tests which one holds attention best.",
         "Dynamic thumbnails, where YouTube shows different thumbnails you picked to different audiences.",
         "Ask Studio, the built-in assistant, can now go through your old videos, suggest new thumbnails and run tests. It's also coming to the mobile app."])
img('insights_research_new.jpg', 6.5, caption='(The new Research page inside Insights, with filters for outlier score and \"Watched by my viewers\". From Creator Insider.)')
img('draft_feedback.jpg', 6.0, caption='(Feedback on a draft video before it\'s published. From Creator Insider.)')
para("Everything in this guide still applies when it reaches you, even if the tab names change again.")

# ================= BUSINESS =================
h1('How A Business Owner Uses These Tabs')
para("If you run a consulting firm, an agency or a coaching business, the goal is getting the right few thousand people to see you and book a call. These tabs are some of the best free market research you'll find for that.")
h2('Your buyers\' search terms are their questions')
para("Every search in Trends and every phrase in YouTube search terms is a question someone typed, in their words. For a service business, that's your FAQ list and your sales objections, written by the buyer.")
para("To show how much demand sits behind those questions, I ran one seed phrase through vidIQ today (October 29, 2026). It estimates monthly YouTube searches:")
table([['Search on YouTube', 'Est. monthly searches', 'Change'],
       ['how to get coaching clients', '63,787', '+202.2%'],
       ['how to get clients from youtube', '40,542', '+28.5%'],
       ['how to get clients on linkedin', '37,457', '+25.3%'],
       ['how to get more clients', '23,677', '-1.4%'],
       ['how to get coaching clients from youtube', '22,665', 'no data'],
       ['how to get agency clients', '21,096', '+165.4%']],
      [3.4, 1.7, 1.4], bold_rows=(0,))
para("Source: vidIQ keyword research, questions mode, 2026-10-29. Treat the numbers as estimates, like the volume labels in Trends.")
para("Say you run a coaching business that helps other coaches sign clients. The search \"how to get coaching clients\" has a vidIQ competition score of 14 out of 100, which is low. That's a video you can make this week, and every person who watches it is the exact person you sell to.")
h2('Who else your buyers watch')
para("\"Channels your audience watches\" is a list of the people your buyers already trust. Study their best videos for topics and pitch them a collab or a guest spot. If you run YouTube ads later, those channels are where your buyers already spend their time.")
para("Even before you have an audience, Trends and the per-video Reach cards start filling in after a few uploads. Use them to check your videos are reaching buyers. If Nate Black's 70% check shows you're being suggested next to entertainment channels instead of business channels, fix the title and the first line of the description before you make more.")
h2('Judge by the right number')
para("Linden Chasteen, who runs YouTube for high-ticket coaches, says business channels should care about audience quality more than impressions. His example: a very niche video with 280 views can bring in more revenue than one with 100,000 impressions, if the right people watched it. Think Media says the same thing in plainer words: the number that matters most is whether YouTube is putting people on your calendar.")
para("So when you read these tabs, ask one extra question: is this search, or this channel, full of people who could buy from me?")
para("**Try this:** Open Trends and search your service in plain words (for example \"bookkeeping for small business\" or \"how to get coaching clients\"). Heart every search a buyer would type before they hire someone like you. Then open \"Channels your audience watches\" and write down the three business channels at the top. That's your topic list and your collab list for the next month.")

# ================= ROUTINE =================
h1('Your 20-Minute Weekly Routine')
para("You don't need to open every tab every day. This is the order I'd go in, once a week, before you plan the next video:")
bullets(["Minutes 1 to 5: Trends. Read \"What people are looking for\" and heart anything new.",
         "Minutes 5 to 10: Audience. Read \"What your audience watches\" (it's only 7 days, so it changes) and note one follow-up idea.",
         "Minutes 10 to 15: Reach on your last video. Copy the top search terms and the top suggesting videos.",
         "Minutes 15 to 18: Pick the idea that shows up in two places, then run it through Inspiration for an outline to beat.",
         "Minutes 18 to 20: Check any A/B test that's running, and start one on an older video if nothing is."], numbered=True)
para("Once a month, add Advanced mode: top five vs bottom five videos over the last 365 days, long-form only.")

# ================= CHECKLIST =================
h1('The Checklist')
checklist(["I opened Studio on a computer (the phone app shows less).",
           "I found the Trends tab (or Research, on older accounts) under Analytics.",
           "I clicked Show all on \"What people are looking for\" and saved at least ten searches with the heart.",
           "I searched each saved phrase on YouTube to see if the current videos are old, off topic or weak.",
           "I noted any search marked as a content gap.",
           "I scrolled down the Audience tab to \"Channels your audience watches\" and \"What your audience watches\".",
           "I wrote the follow-up question for the three most common videos my viewers watched this week.",
           "I opened Reach on my three best videos and copied their YouTube search terms.",
           "I checked \"Content suggesting this video\" and confirmed at least 70% of those videos are aimed at my audience.",
           "I ran one saved search through Inspiration and wrote down what only I can add.",
           "I opened Advanced mode, filtered to Videos, and compared my top five and bottom five.",
           "I started an A/B test on one older video with clearly different options.",
           "If I sell a service, I listed the buyer questions from Trends and the business channels my audience watches."])

# ================= CTA =================
h1('Want Us To Do This For You?')
para("If you'd like a team to do this research for you, then write, edit and package the videos while you just record, that's what we do at Viral Bangers. Book a call and we'll look at your channel together.")
para("**Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]")
