# NICHE lead magnet: "The $44 RPM Niche Map". Voice: Bryan Ng. Data pulled 29 Oct 2026.
# Build: python3 ~/.claude/skills/lead-magnet-doc/scripts/docbuilder.py content.py "The $44 RPM Niche Map.docx" --img-dir img
BOOK = 'https://www.viralbangers.com/book'
def yt(vid, label, t=None):
    return f'[[{label}|https://www.youtube.com/watch?v={vid}' + (f'&t={t}s' if t else '') + ']]'

title_page('The $44 RPM Niche Map',
           [('What 1,000 Views Pays In ', False), ('Every', True), (' Niche', False)], hero='hero.jpg')
toc_page(levels=1)

# ================= TL;DR =================
h1('TL;DR')
para("Two channels can get the exact same 100,000 views and get paid completely different amounts. Going by the Nexlev estimates in this guide, a kids song channel would make about $128 from those views, and a B2B software channel would make about $2,653. The difference is the niche, and who is watching.")
para("I wanted to know what 1,000 views actually pays in every niche, so I pulled real numbers instead of guessing. This guide has the full map: 38 niches, one real video each, with Nexlev's estimate of what that video earns per 1,000 views. I also pulled what creators like Grow With Kaz, Think Media and Shane Hummus have said about their own numbers, and put it all side by side.")
img('chart_rpm_all_niches.png', 6.3, caption='(38 niches, ranked. Blue is where service businesses sell.)')
para("About the $44: Creators in finance report RPMs as high as $50 for 1,000 views. Grow With Kaz puts finance at $15 to $50, and Think Media puts business, finance and real estate ad rates at $20 to $45. So $44 sits inside the range people report for the best money niches. In the Nexlev data I pulled, though, the highest single video estimate was $26.53, with a top estimate of $34.79. I'll show you both, and I'll be straight about which is which.")
para("After the map, you get the 3 checks I'd run before filming a single video in a new niche:")
bullets(["Check 1: are people searching for it? (vidIQ, 5 minutes)",
         "Check 2: who already owns the search results? (one YouTube search, 10 minutes)",
         "Check 3: are small channels breaking out in it right now? (vidIQ or Nexlev, 10 minutes)"], numbered=True)
para("And if you run a business, the last big section is for you. The best paying niches are the exact niches where service businesses sell: finance, real estate, B2B software, legal and health. Your views are worth more than you think. But the ad money is still the smallest part. The client is the money.")

# ================= WHO WE ARE =================
h1('Who We Are')
para("My name is Bryan, and I run Viral Bangers with my co-founder Mauricio. We're a YouTube agency for business owners who sell something, like consultants, coaches, traders and info product businesses. We handle the ideas, the scripts, the editing and the thumbnails, so all you have to do is show up and record. One of the creators we work with is Brad Goh (The Trading Geek), who has over 1.8 million subscribers on YouTube.")
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
img('bryan_course_thumb.jpg', 5.0, caption=f'(A lot of what is in this guide comes from my 3 hour course. {yt("qdE8FKQC_Vg", "Watch it here")}.)')
para("Picking the niche is the first thing we look at with every channel, because if you get it wrong, it doesn't matter how good the videos are. This is the research we use.")

# ================= WORDS =================
h1('Words You Need To Know')
para("Read this once and the rest of the guide gets a lot easier.")
table([['Word', 'What it means'],
       ['RPM', 'Revenue per mille. What you actually get paid for every 1,000 views, after YouTube takes its cut. This is the number that matters.'],
       ['CPM', 'Cost per mille. What the advertiser pays for 1,000 ad views. It is always higher than your RPM.'],
       ['Niche', 'The topic and audience your channel is about. "Real estate for first-time buyers in Dallas" is a niche.'],
       ['Tier 1', 'Viewers in rich countries like the US, Canada, the UK and Australia. Advertisers pay the most to reach them.'],
       ['Mid-roll', 'An ad in the middle of a video. YouTube lets you add them once a video is 8 minutes or longer.'],
       ['Outlier', 'A video that gets far more views than that channel normally gets. A 10x outlier did 10 times its usual views.'],
       ['Saturated', 'A niche where lots of big channels already make the same videos, so a new channel struggles to get seen.'],
       ['Long-form', 'Normal YouTube videos, as opposed to Shorts (vertical videos under 3 minutes).']],
      [1.4, 5.1], bold_rows=(0,))
para("The one that confuses people is RPM against CPM. Think Media Podcast shared a real example where the CPM was $20.49 and the RPM was $7.98. YouTube says creators get 55% of ad revenue, but after views with no ad, ad blockers and everything else, that creator kept about 39% of what advertisers paid. So when someone quotes you a CPM, your take home will be a lot less.")

# ================= $44 =================
h1('Where The $44 Number Comes From')
para("I'm not going to show you a number and pretend it's what everyone gets. Below is what the creators say, then what the data says.")
h2('What creators report')
para("These are the ranges creators have shared about their own channels or their research, pulled from Subscribr's Strategy Search:")
img('chart_creator_reported_rpm.png', 6.4, caption='(The orange line is $44. It sits inside the top of the finance and business ranges.)')
bullets(["Grow With Kaz ranked 20 niches and put finance at $15 to $50 RPM, but said you need real knowledge of the field to do it.",
         "Shane Hummus said finance usually earns $20 to $40 per 1,000 views, and general education earns about $10.",
         "Make Money Matt said real estate investing and make money online both show estimated RPMs over $20.",
         "Think Media Podcast said business, finance, real estate and high-end tech ad rates (CPM) usually sit between $20 and $45.",
         "Think Media also quoted Business Insider research: long-form RPMs between $1.61 and $29.30, and Shorts between $0.04 and $0.06."])
h2('What the data says')
para("Then I went into Nexlev and pulled the numbers myself on 29 October 2026. Two things stood out.")
para("First, Nexlev's niche finder tracks thousands of channels and estimates each one's RPM from its views and revenue. When I filtered for channels above $18 RPM, it returned zero. The highest channels in the whole database sit at about $16.18.")
para("Second, Nexlev has a tool that estimates RPM for one specific video. I ran it on 38 videos across 38 niches. The highest was a 3 hour 20 minute HubSpot CRM tutorial by Drew Brockbank: $26.53 per 1,000 views, with a range of $18.27 to $34.79.")
img('check3_hubspot_outlier.jpg', 6.0, caption='(The highest RPM video in my sample: a HubSpot tutorial from a 16,300 subscriber channel with 51,800 views, 52 times its usual. Next to it, an 18,900 subscriber channel with 23,600 views.)')
para("You can see the same kind of estimate on any channel. In my course I opened Nexlev's analytics on an AI avatar channel that was less than a month old. It showed 4,789,041 views in the last 30 days and an RPM of $2.67, which Nexlev flags as low.")
img('bryan_nexlev_analytics.jpg', 6.0, caption=f'(Nexlev analytics in my video. {yt("qdE8FKQC_Vg", "Watch at 2:10", 130)}.)')
para("So, honestly: $44 is the kind of number finance and B2B creators report at the top end. It is not what the average channel in those niches gets, and no video in my Nexlev sample hit it. Use the map below to see the realistic number for your niche, and treat anything above $30 as a great month.")

# ================= THE MAP =================
h1('What 1,000 Views Pays In Each Niche')
para("This is the full map. For every niche I picked one real, recent video and ran it through Nexlev's RPM estimate. The last column shows what 100,000 views would pay at that rate.")
img('table_rpm_map.png', 6.5, caption='(Every number is an estimate for one real video. Your channel will land higher or lower.)')
para("A few things jump out when you look at it for a while.")
para("B2B software is at the top. People who search \"HubSpot tutorial\" or \"GoHighLevel tutorial\" are business owners about to spend money on software. Advertisers pay a lot to reach them.")
img('thumbs_business_rpm.jpg', 6.5, caption='(Business niches and their estimated RPMs, left to right: HubSpot tutorial $26.53, business credit $14.86, business finance $14.80, GoHighLevel tutorial $12.95, Salesforce course $9.20, QuickBooks demo $6.51.)')
para("Long documentaries beat short clips, even in \"cheap\" niches. A 3 hour true crime video estimated $22.79. A 66 minute history documentary estimated $16.50. A 9 minute kids song estimated $1.28, even with 12 million views.")
img('thumbs_entertainment_rpm.jpg', 6.5, caption='(Entertainment niches, left to right: true crime (3 hours) $22.79, history doc (66 minutes) $16.50, health doc $12.76, police bodycam $10.73, Minecraft $3.38, kids songs $1.28. Length and audience age matter as much as topic.)')
para("Money and property niches sit in the middle when the video is short. A finance reaction video from Zac Rios estimated $7.55. A 9 minute local real estate video estimated $4.76. Same topic as the big numbers creators report, but shorter videos and a wider audience.")
img('thumbs_money_property_rpm.jpg', 6.5, caption='(Finance, real estate and insurance, left to right: finance commentary $7.55, dividend explainer $8.67, mortgage expert $6.62, local agent $4.76, luxury tours $4.18, insurance explainer $4.80.)')
para("Short talking head clips from lawyers and doctors land low on ads. A 6 minute criminal defense video estimated $4.76, and a 5 minute Medicare video from a doctor estimated $2.71. Hold on to that, because in the business section I'll show you why those channels are still some of the most valuable on YouTube.")
img('thumbs_lawyer_doctor.jpg', 6.0, caption='(Lawyer clip $4.76, doctor clip $2.71, elder law $3.14. Low ad RPM, very high client value.)')
para("**Try this:** find your niche in the table, or the closest one to it. Multiply the RPM by the views you think you can get in a month. That's your rough ad income. Write it down, because we'll compare it to what a single client is worth later.")

# ================= WHY =================
h1('Why Finance, Real Estate And B2B Pay More')
para("YouTube runs an auction. Every time an ad shows on your video, advertisers bid to be there. The more money an advertiser makes from one customer, the more they can afford to pay to reach your viewer. YouTube keeps its share, and the creator gets the rest.")
img('bryan_ad_money_drawing.jpg', 5.0, caption=f'(How I drew it in my course: advertisers pay YouTube, YouTube pays creators, viewers bring the money. {yt("qdE8FKQC_Vg", "Watch at 6:00", 360)}.)')
para("Think Media Podcast covered a study of ad rates across seven countries. The seven niches with the highest CPMs were health, business, investing, auto reviews, real estate, insurance and online marketing. Every one of those is a niche where the viewer is about to make a big purchase: a car, a house, an investment, a policy, a piece of software.")
para("Make Money Matt pointed out that the biggest YouTube advertisers include PayPal, Apple, Geico, Expedia, Liberty Mutual and tax companies. If your videos sit next to what those companies sell, you get their budgets.")
para("Age matters too. This is how I explained it in my 3 hour course on starting a channel with Claude:")
para("*\"As a rule of thumb, you want tier one audience, US, Canada, UK, Australia, which will give us $8 RPM, which is kind of the target here. Not like a $2, $3 RPM.\"*")
img('bryan_rpm_target.jpg', 6.0, caption=f'(From my video. {yt("qdE8FKQC_Vg", "Watch this part at 5:00", 300)}.)')
para("The niches I named in that video were real estate, retirement and finance, news, religious content and doctors. They all have an older audience. As I put it in the video, *\"20 to 30 year olds are broke so a lot of older demographic will watch real estate content.\"* Think Media said the same thing in their own words: channels with viewers in their 40s, 50s and 60s earn more per view than channels aimed at Gen Z.")
img('bryan_older_niches.jpg', 6.0, caption=f'(Older audience niches. {yt("qdE8FKQC_Vg", "Watch at 7:00", 420)}.)')

# ================= WHAT CHANGES =================
h1('What Changes Your RPM Inside The Same Niche')
para("Two channels in the same niche can still get paid very differently. These are the levers.")
h2('1. Where your viewers live')
para("Noah Morris shared that a channel with about 80% US viewers tends to land around $7 to $8 RPM. When about 40% of viewers come from India, it drops to around $3, and it can go below $1 if that share goes higher. He also said Canada, Germany and Australia pay well, and the UK pays less than you'd expect.")
img('chart_cpm_by_country.png', 6.0, caption='(Approximate ad rates by country, from Dan the creator.)')
para("Grow With Kaz gave an even bigger gap: a channel with mostly Sri Lankan viewers under $0.30 RPM, compared to around $4 for an international English audience.")
h2('2. How long your videos are')
para("Once a video passes 8 minutes, you can add mid-roll ads. Make Money Matt places them about every 2 minutes, and Mario Joos tested one every minute and saw a small bump in RPM. The Nexlev numbers show how big this effect is.")
img('chart_length_vs_rpm.png', 6.3, caption='(Longer videos almost always estimated a higher RPM in my sample.)')
para("The HubSpot tutorial was 3 hours 20 minutes. The true crime video was 3 hours 7 minutes. The lawyer and doctor clips were 5 to 6 minutes. Don't pad your videos to hit a length, because people will leave and YouTube will stop showing them. But if your topic needs 20 minutes, give it 20 minutes.")
h2('3. Shorts or long-form')
img('chart_shorts_vs_long.png', 5.5, caption='(Same channel, two formats.)')
para("Think Media shared a Short with 11.2 million views that earned $536.74. Their long-form videos on the same channel earned about $30,000 in 28 days at a $7.36 RPM. Grow With Kaz saw the same gap in cooking: $11.25 for long-form and $0.03 for Shorts. If you care about ad money, it comes from long-form.")
h2('4. The time of year')
para("Advertisers spend the most from October to December, then budgets reset in January. Aprilynne Alter shared her first year of YouTube earnings: her lowest day was $9.41 on 15 October, and her highest was $71.48 on 28 November.")
img('chart_q4_days.png', 5.5, caption='(Same channel, six weeks apart.)')
para("Think Media added that some niches have their own peak. Fitness ad rates jump in January for New Year's resolutions, then drop by February and March. Justin Moore said brands often pay two or three times their normal sponsor rate in the fourth quarter, because unspent budget disappears in January.")
h2('5. How old your channel is')
para("Aprilynne also said new channels often start at $2 to $3 RPM and climb to $6 or $7 as YouTube learns who watches. So don't panic if your first month looks low.")

# ================= SKILLS =================
h1('The Skills Each Niche Needs')
para("A high RPM is useless if you can't make the videos. Every niche has a format that works, and every format needs different skills. This table maps them.")
table([['Niche', 'Format that works', 'Skills you need', 'Face?', 'Example from the data'],
       ['B2B software', 'Screen-recorded tutorials, full walkthroughs', 'Know the tool, record your screen, clear voiceover', 'Optional', 'Drew Brockbank (HubSpot), Tutorial Stack'],
       ['Business finance and credit', 'Talking head, long slide explainers', 'Real expertise, simple slides', 'Usually', 'Jack McColl, BizMoney Explained'],
       ['Personal finance', 'Reaction commentary, illustrated explainers', 'Personality, or simple drawings and a calm voice', 'Either', 'Zac Rios, Drawn Investor'],
       ['Real estate (local)', 'Talking head, area tours, buyer mistakes', 'Local knowledge, filming on location', 'Yes', 'Jamie Hering (Chicago suburbs)'],
       ['Mortgage and housing', 'Expert talking head, market updates', 'Explaining numbers simply', 'Yes', 'Nathan Udomsri'],
       ['Legal', 'Talking head scripts ("say this to the police")', 'Licence, short punchy scripts', 'Yes', 'Law Office of John Guidry, Landmark Legal'],
       ['Health and Medicare', 'Doctor talking head, long explainers', 'Credentials, trust, calm delivery', 'Yes', 'SliceofLifeMD, CalHealth'],
       ['Insurance', 'Faceless explainers', 'Clear scripts, stock visuals, voiceover', 'No', 'Insurance About YouTube'],
       ['True crime and history', 'Long faceless documentaries', 'Research, storytelling, narration, archive footage', 'No', 'Uncoverd Crimes, Orca Planet TV'],
       ['Health stories', 'Commentary documentaries', 'Clip editing, story structure', 'No', 'Big Craig'],
       ['Reddit stories', 'Narrated stories over a visual', 'Voice and volume of output', 'No', 'KoleReads'],
       ['Kids and gaming', '3D animation, gameplay', 'Animation or gaming skill', 'No', 'Baby Bon Bon, Grin and Game It']],
      [1.1, 1.4, 1.6, 0.6, 1.8], bold_rows=(0,))
para("The top half of that table is talking head and screen recording. The bottom half is mostly faceless. Make Money Matt has covered how faceless channels are made: screen recording with OBS and a voiceover for tutorials, whiteboard animation for finance, stock footage and voiceover for health. Think Media made the point that faceless has its own kind of hard work: you need a visual for every line and much stronger editing, because there's no face to hold attention.")
para("One warning if you're thinking about an AI-voice faceless channel. Make Money Matt and Dan the creator both covered YouTube's change from \"repetitious\" to \"inauthentic\" content. Channels that scrape Reddit stories with a robotic voice, or mass-produce videos from one template, are the ones getting hit. Add real human input or don't bother.")
para("**Try this:** pick two niches from the map that pay well. Next to each one, write the format and the skills it needs. Circle the one you could make 20 videos in without hating your life. That's your niche.")

# ================= 3 CHECKS =================
h1('How To Check A Niche Is Still Empty')
para("A niche that pays well still has to pass two more tests: people want it, and you can still get seen. These 3 checks take about 25 minutes. I'll walk you through each one on a real niche: GoHighLevel and HubSpot tutorials, the B2B software niche at the top of the map.")
img('bryan_claude_niche.jpg', 6.0, caption=f'(Me using Claude and the Subscribr tools to find a niche. {yt("qdE8FKQC_Vg", "Watch at 14:30", 870)}.)')

h2('Check 1: Are people searching for it?')
para("**Step 1.** Open vidIQ and go to keyword research. Type the main thing your niche is about, like \"gohighlevel tutorial\".")
para("**Step 2.** Look at two numbers: estimated monthly searches and competition (0 to 100, lower is easier). Make Money Matt sorts by vidIQ's overall score, which weighs the two together.")
para("**Step 3.** Ignore the giant keyword. Look for a related keyword with real searches and competition under about 25.")
para("This is what came back on 29 October 2026:")
img('chart_check1_keywords.png', 6.3, caption='(The orange dots are the openings.)')
table([['Keyword', 'Monthly searches', 'Competition', 'Trend'],
       ['gohighlevel tutorial', '124,609', '63', '-4.6%'],
       ['hubspot crm tutorial for beginners', '71,438', '44', '-0.9%'],
       ['hubspot tutorial', '32,641', '22', '-27.1%'],
       ['hubspot crm tutorial', '10,794', '34', '+230.7%'],
       ['gohighlevel funnel tutorial', '8,989', '15', '+79.4%'],
       ['gohighlevel funnels', '4,699', '16', 'not shown']],
      [2.6, 1.4, 1.2, 1.3], bold_rows=(0,))
para("\"Gohighlevel tutorial\" has 124,609 searches, but a competition score of 63. \"Gohighlevel funnel tutorial\" has 8,989 searches, a competition score of 15, and it's growing 79.4%. That's the one I'd test first. Marcus Jones calls this trading search volume for a better chance of ranking, and his example was \"upload shorts from PC\" at 100,000 searches against \"upload shorts from Mac\" at 1,200 with far less competition.")
para("**Pass if:** you can find 3 or more keywords in the niche with competition under about 25 and a few thousand searches.")

h2('Check 2: Who already owns the search results?')
para("Noah Morris checks saturation like this: take the core of a popular title in the niche, search it on YouTube, and look at how many channels are making the exact same video, especially big old channels.")
para("**Step 1.** Search your best keyword from Check 1 on YouTube (or use Nexlev's YouTube search to get the view counts in one list).")
para("**Step 2.** Write down the views and age of the top 20 results.")
para("**Step 3.** Count how many have over 100,000 views, and how many are less than a year old.")
img('chart_check2_saturation.png', 6.3, caption='(Top 20 results for "gohighlevel funnel tutorial", 29 October 2026.)')
para("Only one of the top 20 has over 100,000 views: Charlie Chang with 580,668. Most of the rest are under 5,000 views, and a lot of them are a year old. One result is a 4 hour 46 minute Tagalog version from Kuys RJ that got 59,533 views in 6 months, which tells you a longer, more complete video can still break through here.")
img('check2_top_results.jpg', 6.5, caption='(The three biggest results: Charlie Chang with 580,668 views, Funnel Scene with 53,139 and Kuys RJ (in Tagalog) with 59,533.)')
para("Compare that to what Noah called saturated: Mike Tyson fight documentaries and police bodycam. In those, early low-quality videos used to go viral, but now you're up against big channels like Law&Crime BodyCam, with 572,000 subscribers and an estimated $64,673 a month.")
img('noah_saturation.jpg', 6.0, caption=f'(Noah Morris showing his saturation search. {yt("E5IzG1q0M14", "Watch his video", None)}.)')
para("Marcus Jones adds one more thing to look at. If you have vidIQ installed, it shows the subscriber count next to each result. Small channels (1,000 to 10,000 subscribers) ranking on page one is a good sign. Page one full of 500,000+ subscriber channels is a bad one.")
para("**Pass if:** fewer than 5 of the top 20 results have 100,000+ views, and at least a few small channels rank on page one.")

h2('Check 3: Are small channels breaking out right now?')
para("This is the one I trust most. In my course I put it like this: *\"Look for proof from smaller recent channels, one or two months old, and already pulling big numbers.\"* If a small channel just got a huge video in your niche, the niche is live right now.")
img('bryan_proof_small.jpg', 6.0, caption=f'(From my video. {yt("qdE8FKQC_Vg", "Watch at 11:01", 661)}.)')
para("**Step 1.** Open vidIQ outliers (or Nexlev's viral videos from small channels). Type your niche as a topic.")
para("**Step 2.** Set the maximum channel size to 50,000 subscribers and the date to the last 6 months.")
para("**Step 3.** Look for videos doing 10x or more of their channel's normal views. Paddy Galloway looks for outliers at 3x to 50x a channel's average, and Noah Morris checks that the same topic breaks out on more than one small channel, so it isn't luck.")
para("For B2B software, Drew Brockbank's HubSpot tutorial did 51,800 views on a 16,300 subscriber channel, 52x his normal views. Tutorial Stack, at 18,900 subscribers, has a GoHighLevel tutorial with 23,600 views. Both are monetized at some of the highest RPMs in the map.")
para("Then I ran the same check across the service-business niches. These are all small channels with breakout videos in the last 6 months:")
img('chart_check3_outliers.png', 6.3, caption='(Small channels, big breakouts, all in high value niches.)')
img('thumbs_service_outliers.jpg', 6.5, caption='(Left to right: 2,500 subs, 81,800 views. 29,500 subs, 44,700 views. 12,200 subs, 346,000 views. 6,900 subs, 205,500 views. 43,600 subs, 107,500 views. 1,100 subs, 66,400 views.)')
para("SliceofLifeMD, a doctor with 12,200 subscribers, got 346,000 views on one Medicare video. That's 1,804 times his normal views. Landmark Legal, with 2,500 subscribers, got 81,800 views on a video about police tricks. John Farrell, with 1,100 subscribers, got 66,400 views on a real estate video.")
para("If you want to go deeper, the creator howtoai showed a Nexlev filter for finding live niches: channels created in the last 90 days, with at least 10,000 subscribers and at least $3,000 a month. His example was a psychology and social skills channel that was 3 months old, with nearly 50,000 subscribers and about $4,000 a month.")
para("**Pass if:** you find at least 3 videos from channels under 50,000 subscribers doing 10x their normal views in the last 6 months, on at least 2 different channels.")
para("If a niche passes all 3 checks, film. If it fails one, go narrower (Shane Hummus calls this being the king of a puddle) and run the checks again.")
para(f"If you'd rather have us run this research for your business and tell you which videos to make first, that's what we do. **You can book a call here:** [[viralbangers.com/book|{BOOK}]]")

# ================= PAY FOR ITSELF =================
h1('Will The Niche Pay For Your Videos?')
para("This is the simple math I walk people through on our Subscribr calls. You need three numbers: your RPM (from the map), your view ceiling (the most views the biggest videos in your niche get), and your cost per video.")
table([['', 'Channel A', 'Channel B'],
       ['RPM', '$3', '$3'],
       ['Cost per video', '$300 (editor $250, thumbnail $50)', '$800'],
       ['Views needed to break even', '100,000', '266,667'],
       ['Typical big hit', '1,000,000 views, 1 in 10 videos', '500,000 views'],
       ['What the big hit pays', '$3,000, covers 10 videos', '$1,500, covers 1.9 videos']],
      [1.9, 2.3, 2.3], bold_rows=(0,))
para("Channel A works, because one big video pays for the other nine. Channel B doesn't, unless it lowers its costs or moves to a niche with a higher RPM or a higher view ceiling.")
para("**Try this:** take the RPM for your niche from the map. Divide your cost per video by that RPM, then multiply by 1,000. That's how many views each video needs to pay for itself on ads alone.")

# ================= BUSINESS =================
h1('If You Run A Business, Ad Revenue Is The Smallest Part')
para("If you sell a service, this is the most important part of the guide. Look at the map again. The niches where ad rates are high (finance, real estate, B2B software, legal, health, insurance) are the same niches where service businesses sell. Advertisers pay more to reach your viewers because those viewers buy expensive things. You're the one selling the expensive thing.")
table([['If you sell...', 'Your niche on the map', 'Estimated RPM from the data'],
       ['Accounting, bookkeeping, fractional CFO', 'Business finance, bookkeeping', '$6.51 to $14.80'],
       ['Software, SaaS, agency services', 'B2B software tutorials', '$12.95 to $26.53'],
       ['Business loans, credit, funding', 'Business credit and funding', '$14.86'],
       ['Mortgages, real estate', 'Mortgage and housing, home buying', '$4.18 to $6.62'],
       ['Legal services', 'Criminal defense, police rights', '$2.41 to $4.76'],
       ['Health, Medicare, elder law', 'Medicare, health', '$2.71 to $12.76'],
       ['Insurance', 'Life insurance explainer', '$4.80'],
       ['Financial advice, investing', 'Dividend, personal finance', '$2.58 to $8.67']],
      [2.3, 2.3, 1.9], bold_rows=(0,))
para("Even at the top of the map, ad money is small next to one client.")
img('chart_ads_vs_client.png', 6.3, caption='(Ad revenue on a great video, compared to one client.)')
para("Shane Hummus has a client with a recruiting agency for a hard-to-fill role. Their videos get about 100 views each. At the best RPM in my whole map, 100 views pays $2.65 in ads. But every one of those viewers is a business owner or executive, and one placement pays up to $50,000. Shane says that channel brings in about $2 million a year. He has another client, an IT support company, that gets about 500 views a video and does about $10 million a year.")
para("Think Media shared a real estate agent who got a $1.8 million listing from a client who had watched six hours of her videos. They signed on the first appointment, because the videos had already done the selling. Think Media also cited a study that 42% of people are more likely to hire a service provider who has a YouTube channel.")
para("Shane also broke down Law By Mike, a lawyer whose content feeds his own firm's practice areas, personal injury and criminal defense. The videos are a lead source that runs 24 hours a day.")
para("I've said this in one of my own videos: for a B2B business, one B2B view can be worth as much as 10,000 regular views, because that viewer is someone you can actually sell to.")
para("So when you look at the map, look at it two ways. The RPM tells you YouTube will pay you more than you'd expect for your niche, which helps cover the cost of the videos. The client is what makes the channel worth it.")
para("**Try this:** take the monthly ad number you wrote down earlier. Now write down what one new client is worth to you over a year. If one client a month from YouTube beats your ad income, and for almost every service business it will, plan your videos around getting clients, and treat the ads as a bonus.")

# ================= CHECKLIST =================
h1('The Checklist')
checklist(["Found my niche (or the closest one) in the map and wrote down its RPM",
           "Multiplied that RPM by the views I think I can get in a month",
           "Checked that my target viewers are mostly in tier 1 countries and over 25",
           "Planned long-form videos over 8 minutes where the topic needs it",
           "Picked a format I can make 20 videos in, and listed the skills it needs",
           "Check 1: found 3+ keywords with a few thousand searches and competition under 25",
           "Check 2: fewer than 5 of the top 20 results have 100,000+ views",
           "Check 2: small channels rank on page one",
           "Check 3: found 3+ breakout videos (10x or more) from channels under 50,000 subscribers in the last 6 months",
           "Worked out how many views each video needs to pay for itself on ads",
           "Wrote down what one client is worth to me, and compared it to my monthly ad income"])

# ================= CTA =================
h1('Want Us To Do This For You?')
para("If you run a business and want YouTube to bring you clients, we'll do the niche research, the ideas, the scripts, the editing and the thumbnails. You show up and record. On the call we'll look at your niche, your offer and what a viewer is worth to you, and tell you exactly what we'd make first.")
para(f"**Book your 30-minute strategy call here:** [[viralbangers.com/book|{BOOK}]]")
