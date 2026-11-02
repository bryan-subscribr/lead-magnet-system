# Phase 2: Systems (2.1 packaging, 2.1a packaging teardown, 2.2 scripting, 2.2a hook critique, 2.4 funnels + tracking, 2.5 team)
# Screen-share style (STYLE_V2.md). Builder: tools/docbuilder_ss.py. Images: img/p2_*.

# ================= 2.1 PACKAGING =================
h1('Packaging: Titles And Thumbnails', stat='RP Profits: 2,393 to 17,517 median views')
para('Order of work on every video: idea, then title, then thumbnail, then script, then filming. The title, thumbnail and idea drive 80 to 90% of how a video does. If an idea can\'t be packaged, the script shouldn\'t exist.')
para('Every time I wrote the script first and packaged it at the end, the video flopped.')
flow([('Step 1', 'Idea'), ('Step 2', 'Title'), ('Step 3', 'Thumbnail'), ('Step 4', 'Script'), ('Step 5', 'Film + edit')], name='p2_flow_order.png')

h2('Why It Matters')
bullets([
    'YouTube shows a viewer about 8 videos at a time. One gets the click and the other seven lose.',
    'The best video in the world loses if its title and thumbnail don\'t win that click.',
    'I split it 50/50 between the thumbnail and the title.',
])
img('p2_feed.jpg', 6.0, caption='(From my 3-hour course: one winner per feed, seven losers.)')

h3('The Chain')
flow([('Sells', 'Thumbnail'), ('Sells', 'Title'), ('Sells', 'Hook'), ('Sells', 'Intro'), ('Sells', 'Rest of video')], name='p2_flow_chain.png')
para('The thumbnail sells the title, the title sells the click, the click sells the hook. For a business, the goal is the right person clicking. Optimize the thumbnail for your ideal customer, and random views come second.')

h2('A Thumbnail Has Two Jobs')
img('p2_two_jobs.jpg', 6.0, caption='(Slide from my thumbnail course, the Thumbnail Codex.)')
bullets([
    ('Stop the scroll', ['Faces, large numbers, money, danger, emotion, bright colours, or something aesthetically pleasing.']),
    ('Open a curiosity gap', ['The gap between what the viewer knows now and what they want to know.', 'If you can\'t state the gap in one sentence, it isn\'t strong enough.']),
])
para('A thumbnail has to do both. Stopping the scroll and getting the click are different jobs.')

h2('Rules I Use On Every Thumbnail')
stack([
    ('Three elements max', 'legible on mobile'),
    ('Match the face to the video', 'serious video, serious face'),
    ('Thumbnail matches the first frame', 'no catfishing'),
    ('Text: 5 words max, sans-serif', 'never the title\'s words'),
    ('Main character dominates the text', ''),
    ('One format, reused', 'when it works, double down'),
], title='Thumbnail Rules')
img('p2_rule_of_3.jpg', 6.0, caption='(Rule of three: every element readable at phone size.)')
para('I treat thumbnails as engineering. A thumbnail with three elements tells the eye where to land first. Anything past three is clutter on a phone screen.')

h3('Title Head: The Simplest Format For A Founder')
img('p2_title_head.jpg', 6.0, caption='(Title head: face on one side, short text on the other.)')
para('Face on one side, simple text on the other. Repeating your face builds familiarity with the person the viewer should trust. It is the base of RP Profits\' formula below.')

h3('My Own Mistake')
img('p2_lasik.jpg', 6.0, caption='(My early thumbnail had glasses. By then I\'d had LASIK and didn\'t wear them in the video.)')
para('I got LASIK and didn\'t take new thumbnail photos, so my thumbnails showed glasses and my videos didn\'t. Make sure the thumbnail matches the first frame so you don\'t catfish your viewers. Do a dedicated photo shoot for thumbnail faces. Screenshots from a recording are lower resolution, with bad lighting and unflattering angles.')

h2('Case: RP Profits')
label('Channel:', '[[@RPProfits|https://www.youtube.com/@RPProfits]] · day trader, sells trading education')
img('p2_rp_numbers.jpg', 6.5, caption='(RP Profits. Median views per video, and formula videos vs the rest.)')
stack([
    ('Median views per video', '2,393 to 17,517'),
    ('31 formula videos vs the other 33', '20,007 vs 4,501 average (4.4x)'),
    ('Same words, old design vs formula', '2,887 to 25,031 views'),
    ('4 months off the formula', '30 videos, 4,197 average'),
    ('One formula thumbnail inside that slump', '12,356, beat 29 of the 30'),
], title='The Numbers')

h3('Before: A Screenshot As The Thumbnail')
img('p2_rp_before.jpg', 4.5, caption='(Before we started: a chart screenshot with the URL bar showing.)')

h3('His Own Fix: Every Video Looked Like A Different Channel')
img('p2_rp_own_fix.jpg', 6.5, caption='(Better titles, but every thumbnail in its own visual language.)')
img('p2_rp_three_looks.jpg', 6.5, caption='(His three best videos from that phase: three unrelated looks.)')
para('RP fixed the design himself and views stayed flat. Each of his 32 videos in that phase had its own look. A viewer who saw 4 of his videos had seen what looked like 4 different channels, so nobody recognised him.')
para('Buyers usually buy after watching several of your videos. They have to know it\'s you every time.')

h3('After: One Formula, Reused')
img('p2_rp_formula_pair.jpg', 6.5, caption='(Two formula thumbnails months apart. The chart and the 2 or 3 words change.)')
img('p2_rp_formula_grid.jpg', 6.5, caption='(The formula on every upload since August 2025.)')
bullets([
    'A real chart: his buyer recognises their own world in a split second.',
    'Two markers on the chart show the result and hide the how.',
    'A calm face says he knows what he is doing.',
    'Dark background, so it stands out in a bright feed.',
])

h3('Same Words, Different Wrapper')
img('p2_rp_same_words.jpg', 6.5, caption='(Left: "9:30 AM EVERYDAY" on the old design, 2,887 views. Right: the same words on the formula.)')
para('"9:30 AM EVERYDAY" on the old bright design got 2,887 views. The same words on the formula averaged 25,031 across 7 videos.')

h3('The Accidental Test')
img('p2_rp_slump_grid.jpg', 6.5, caption='(The 4 months off the formula.)')
img('p2_rp_slump_winner.jpg', 4.5, caption='(The one formula thumbnail inside the slump: 12,356 views.)')
para('We dropped the formula for 4 months. 30 videos averaged 4,197. One formula thumbnail in the middle of that stretch got 12,356 and beat 29 of the 30 around it, in the same month, with the same audience and the same offer. With a written formula, "did the audience change?" becomes a 4-second check.')

h2('Show Your Buyer\'s Version Of The Chart')
img('p2_instantly_slide.jpg', 6.0, caption='(Instantly AI\'s thumbnail, from my 3-hour course.)')
para('Instantly AI\'s thumbnail shows a Stripe dashboard: $10,000 monthly revenue and a graph going up. The graph is purple on purpose, because business owners know the Stripe graph on sight. The thumbnail shows the dream outcome in a format the buyer already looks at.')
para('For a trader that object is a candlestick chart. Find yours by answering two questions:')
bullets([
    'What screen, document or number does my buyer look at every week?',
    'What does it look like when they\'ve won?',
], numbered=True)
para('Put one concrete, readable object in every thumbnail. If the idea can\'t be drawn, the title is too vague.')

h2('Thumbnail Text And Title Work Together')
img('p2_congruence.jpg', 6.0, caption='(Title and thumbnail make one promise.)')
bullets([
    'Never repeat the title on the thumbnail. The text adds something the title doesn\'t say.',
    'Both make the same promise in different words.',
    ('Example from RP', ['Thumbnail: "It\'s so f*cking simple."', 'Title: "I Made $750,000 In A Year With This Super Easy Scalping Strategy" (his title, his number)']),
    'I generate titles until I get one I\'m happy with.',
])

h2('Three Checks Before Upload')
img('p2_three_tests.jpg', 6.0, caption='(The three tests, from my 3-hour course.)')
table([
    ['Test', 'Question'],
    ['Clarity', 'Can you see every element at the smallest YouTube size?'],
    ['Contrast', 'Does it stand out next to competitor thumbnails?'],
    ['Glance', 'Show it to someone for 2 seconds. Do they understand it?'],
], [1.4, 5.0])

h2('Testing')
bullets([
    'The only click-through baseline is your own channel\'s. No videos yet: use 5%.',
    'Test only when CTR is under your 24-hour, 7-day or 30-day average.',
    'Test the thumbnail first, then the title. Change one variable per test.',
    'New upload: publish with the best thumbnail, run an hourly test with 4 to 5 variations, end early if there\'s a clear winner.',
    'Old videos can come back with a new title and thumbnail. YouTube is evergreen.',
])

# ================= 2.1a TEARDOWN =================
h1('Packaging Teardown: Worked Examples')
para('I score every thumbnail on the same five checks, in this order.')
img('p2_click_checklist.jpg', 6.0, caption='(My thumbnail checklist.)')
table([
    ['#', 'Check', 'Pass if'],
    ['1', 'Curiosity gap', 'You can state it in one sentence'],
    ['2', 'Thumbnail type', 'Right type for this video (title head, result, transformation...)'],
    ['3', 'Rule of three', 'Three elements or fewer'],
    ['4', 'Hierarchy', 'On first glance the eye goes to one thing'],
    ['5', 'Clarity, contrast, glance', 'Passes all three tests'],
], [0.4, 1.9, 4.1])

h2('Example 1: My Own Thumbnail')
img('p2_lasik.jpg', 5.5)
stack([
    ('Fails', 'Thumbnail doesn\'t match the first frame'),
    ('Fix', 'New photo shoot, same face as the video'),
])

h2('Example 2: RP Profits Before And After')
img('p2_rp_three_looks.jpg', 6.5, caption='(Before: dark chart, lifestyle split, shocked face with money.)')
img('p2_rp_formula_pair.jpg', 6.5, caption='(After: one format.)')
stack([
    ('Fails', 'No repeat look, so no recognition'),
    ('Fix', 'Design one thumbnail and reuse it. Change only the chart and the words.'),
])

h2('Example 3: Instantly AI')
img('p2_instantly_slide.jpg', 5.5)
stack([
    ('Passes', 'One object the buyer knows (the Stripe graph) showing the dream outcome'),
    ('Rule', 'Show your buyer\'s version of the chart'),
])

h2('Titles: What Changes The Click')
bullets([
    'Name a specific result, number or object the viewer wants.',
    'Leave your inner life out of the title. Buyers click on a result they want.',
    'Use first person when it is your result.',
    ('Show over tell', ['"YouTube settings" style videos can get views, but the viewers don\'t buy from you.', 'Oscar Owen\'s "I showed Will Brown how to make $750,000 per month on YouTube" shows the result on someone else. It may get a fraction of the views, and it sells.']),
])
para('Confused people don\'t subscribe to your channel and they don\'t buy from you.')

# ================= 2.2 SCRIPTING =================
h1('Scripting: Aha Density', stat='Over a thousand scripts written')
stack([
    ('Value', 'shows people what to do'),
    ('Insight', 'shows them why it works and where to look'),
], title='Value vs Insight')
img('p2_value_insight.jpg', 6.0, caption='(From my scriptwriting system video.)')
para('Value can be copied from others. Insight comes from your own experience.')

h2('Example: My Bullet-Point Script Video')
bullets([
    'Value version: "write a bullet-point script." The viewer doesn\'t know why it matters, so they might not even do it.',
    ('Insight version: the story', ['November 2023: 2 months on a 10-minute script.', 'Recording took 10 hours.', 'The script didn\'t feel natural.']),
    'The insight I wanted to leave: a full word-for-word script felt unnatural. So I write bullet points, and only the hook is fully written.',
])

h2('Scripts Get Written More Than Once')
bullets([
    'My 90-minute course video: draft one was bad, draft two was still bad, draft three was good enough to get 250,000 views.',
    'Editing your script is where you find gold.',
    'Come back the next day. With fresh eyes I see 10 times more writing mistakes.',
    'Your first draft doesn\'t have to be amazing. It just has to exist.',
])

h2('The Hook')
para('The hook is what convinces the viewer to watch the rest of the video. I spend 50% of my remaining scripting time refining it. Nail it and 30-second retention can hit 50 to 60%, sometimes 70%.')
img('p2_edu_hook.jpg', 6.0, caption='(From "I Scripted 1000 YouTube Videos".)')
para('Standard hook advice is validate the click, establish context, set expectations. It breaks for education videos. Nothing life or death is on the line, so there\'s no context to set up, and the content is too deep to sum up in a line.')

h3('Proof, Desire, Value')
table([
    ['Part', 'What it does', 'Example'],
    ['Proof', 'Why you are worth listening to. Must be something your audience cares about. Don\'t overdo credentials.', 'Revenue, client results'],
    ['Desire', 'This video gets them their dream outcome', 'Your first $10,000 a month'],
    ['Value', 'What they get from watching', 'Often just the title, repeated'],
], [0.9, 3.5, 2.0])
para('Every hook needs all three. Miss one and the video won\'t make it. I came up with this after writing for 40+ educational channels.')

h2('Example: My 90-Minute Course Hook')
label('Video:', '[[Full YouTube Script Writing Course (1+ Hour)|https://www.youtube.com/watch?v=YrQvEUZVXy8]] · the video behind $275,766')
img('p2_hook_doc.jpg', 6.0, caption='(The hook on screen in my breakdown video.)')
table([
    ['Line', 'Job'],
    ['"I don\'t know a whole lot about YouTube... my thumbnails are okay, but if there\'s one thing that I\'m good at, it\'s how to write a great YouTube script."', 'Concession. Admitting a weakness makes me relatable.'],
    ['"In the last 9 months I\'ve written YouTube scripts for 40 plus educational channels... Instantly AI, Hypefury, and Davie Fogarty..."', 'Proof, front-loaded'],
    ['"...how to write a killer YouTube script that will get you millions of views."', 'Desire'],
    ['The module list: video ideas, my 5-step system, hook, body, CTA, breakdowns', 'Value'],
], [4.4, 2.0])
para('This hook is long on purpose. 30-second retention may be worse, but a 90-minute video has to sell the viewer on watching the whole thing. For a 10-minute founder video, keep the hook within 30 seconds.')

h2('Example: Jordan Welch, 923,571 Views')
label('Video:', '[[getting rich is easy, actually|https://www.youtube.com/watch?v=9SWaq5Eoak0]] · we scripted it')
img('p2_jordan_video.jpg', 6.0)
img('p2_jordan_line1.jpg', 5.5, caption='(Line 1 on screen.)')
table([
    ['#', 'Line', 'Part'],
    ['1', '"What if I told you that getting richer than 99% of people is actually easier than you think and all it takes is just 30 minutes a day?"', 'Desire'],
    ['2', '"...I promise you will make more progress in one year than most people will in a lifetime."', 'Desire'],
    ['3', '"I started doing this a few years ago when I was completely broke and today even after making over $10 million online..."', 'Proof'],
    ['4', '"So today, I\'m going to share it with you and tell you why it worked so well and show you how you can apply it..."', 'Value'],
], [0.3, 4.9, 1.2])
para('Line 3 works because the proof is specific. A real number makes people believe you.')

h2('The Body')
bullets([
    'Start every block with the why.',
    'Keep only what the viewer needs to know. They care about what is relevant to them, and nobody needs it complete.',
    'Viewers leave when they see no reason to stay.',
    'Close every open loop. An unresolved loop feels like a broken promise.',
])

h2('My Script Pass')
flow([('1', 'Rough first draft'), ('2', 'Write the hook'), ('3', 'Fit content to the hook'), ('4', 'Cut, next day')], name='p2_flow_script.png')
bullets([
    'Your content fits into your hook. The hook never gets bent to fit the content.',
    'To edit is to cut.',
])

h2('Mistake We See')
para('A long welcome or bio before any proof. If you watch my first 10 videos you probably wouldn\'t even see me smiling. A good edit can\'t save a bad script, and a good script can save a bad edit.')

# ================= 2.2a HOOK CRITIQUE =================
h1('Hook Critique: Worked Examples')
para('One point each for Proof, Desire and Value. A hook needs 3 out of 3.')
table([
    ['Hook', 'Proof', 'Desire', 'Value', 'Score'],
    ['My 1+ hour course', '40+ channels, Instantly AI, Hypefury, Davie Fogarty', 'Scripts that get millions of views', 'Module list', '3/3'],
    ['Jordan Welch, 923,571 views', 'Broke to $10 million online', 'Richer than 99%, 30 minutes a day', '"Share it... show you how you can apply it"', '3/3'],
], [1.4, 1.6, 1.4, 1.4, 0.6])
bullets([
    ('My own hook', ['Weak spot: it\'s long, so 30-second retention may be worse.', 'Kept because the video is 90 minutes and has to sell the whole watch.']),
    ('Jordan\'s hook', ['Line 1 is a question. In our own scripts we write hooks as direct statements.']),
])
img('p2_hook_doc.jpg', 5.5)
para('Rewrite rule for any hook that scores below 3: find the missing part and pull it from later in the video. Proof often sits a few minutes in and belongs in the first 30 seconds.')

para("**Book your 30-minute strategy call here:** [[viralbangers.com/book|https://www.viralbangers.com/book]]")

# ================= 2.4 FUNNELS =================
h1('Funnels And Tracking', stat='Every booked call traced to a video')
para('Once a video gets traffic, send the viewer to a landing page. Get them out of YouTube. A YouTube funnel takes someone from never having heard of you, to one video, to several videos, to buying.')

h2('Tracking Comes First')
para('Track every booked call back to the video it came from, before the next upload. You can\'t run a company on likes.')
stack([
    ('One link per video', 'description line 1 + pinned comment'),
    ('One question on the booking form', '"Which video sent you here?"'),
    ('Measure', 'qualified calls booked per week, per video'),
], title='Free Tracking Setup')
para('For Scott Taylor we set it up so every booked call could be traced back to the video it came from. Before that he was convinced his channel was restricted. It wasn\'t. Most of his clients were coming from ads, and nobody could tell which videos were bringing in money.')

h2('Funnel 1: Book A Call (Ours)')
flow([('TOF', 'YouTube video'), ('Page', 'Headline + VSL + proof'), ('Qualify', 'Application form'), ('Close', '30-min strategy call')], name='p2_flow_bookcall.png')
img('p2_vb_home.jpg', 6.0, caption='(viralbangers.com: headline, VSL, book-a-call button.)')
bullets([
    ('The page', ['A headline, a video sales letter, and a book-a-call button.', 'The VSL answers the questions in the prospect\'s mind. Mine is 2 minutes because the education cycle is short. Some are 5 or 10.', 'It can be a PowerPoint or you talking over a Google Doc. No heavy editing.']),
    ('Qualify', ['Selling $3,000+: qualify before the call so you don\'t get on with someone who can\'t afford you.', 'Our form asks current monthly revenue and what you sell at what price.']),
    ('After booking', ['Confirmation email with a one-pager and a short video, reminders, and a day-of email.', 'Qualified people who don\'t book get an 18-email booking-recovery sequence.']),
    'Selling low ticket (software, info products): skip the call and send them direct to checkout.',
])
para('A client once told me he found me from someone else\'s YouTube channel. He searched my name, watched one video, filled in the form, booked and paid in full.')

h2('Funnel 2: Webinar')
flow([('TOF', 'YouTube video'), ('Register', 'Webinar sign-up'), ('Event', 'Webinar'), ('Close', 'Sale or call')], name='p2_flow_webinar.png')
label('Client:', 'Fiction Profits Academy · $3 million to $4 million a month from paid ads')
img('p2_fpa_search.jpg', 6.5, caption='(#1 on YouTube for "how to start a KDP business".)')
img('p2_fpa_channel.jpg', 5.5, caption='(7,000 to 15,000 subscribers, 500,000+ views.)')
bullets([
    'They already spent heavily on ads and needed a nurturing layer.',
    'When people search Fiction Profits Academy, their educational videos come up. That works as the middle of the funnel and feeds webinar registrations.',
    'The scripts are tight enough that they don\'t review them. The main person just records.',
    'More revenue is attributed to YouTube, but it isn\'t tracked yet.',
])
label('Client:', 'Scott Taylor')
img('p2_scott_webinar.jpg', 6.0, caption='(One last-minute video: about 200 webinar registrants in 72 hours.)')
para('Webinar CTA tip: link the video to another of your videos, and that one to the webinar. Viewers who watch more than one video convert better.')

h2('Which One To Run')
table([
    ['', 'Book a call', 'Webinar'],
    ['Price point', '$3,000+', 'Any; low ticket can go direct to checkout'],
    ['Needs', 'Someone on calls, qualifying questions', 'A presenter and a live date'],
    ['Breaks when', 'Unqualified calls waste your time', 'The offer keeps changing, low attendance'],
    ['Measure', 'Booked calls per video', 'Registrants per video'],
], [1.3, 2.5, 2.6])
bullets([
    'Already spending heavily on ads: start with search videos (the Fiction Profits model).',
    'No ad machine: start with browse videos (the Scott model).',
])

h2('Third Path: Lead Magnets')
flow([('Video', 'Comment keyword'), ('DM', 'Guide + email ask'), ('Email', 'Sequence'), ('Close', 'viralbangers.com/book')], name='p2_flow_leadmagnet.png')
bullets([
    '9 guides, one comment keyword each: SCRIPT, SCOTT, EDIT, THUMBNAILS, MILLION, ALGORITHM, IDEAS, SETUP, CLAUDE.',
    'The DM sends the guide and asks for the email. Every email in the sequence ends on the booking link.',
    'A newsletter opt-in feeds the same welcome flow.',
])

h2('Mistake We See: Too Many Steps')
label('Client:', 'Clover Trading')
bullets([
    ('Old funnel: 9 steps', ['A free course needed a 30-minute questionnaire and two separate logins.', 'No VSL anywhere.']),
    'We spent our first five months making videos for that funnel. Views went up a lot and almost none of it converted.',
    ('New funnel: 3 steps', ['A VSL, an application, a booked call.']),
    'We now audit the offer and the funnel before making a single video.',
])
flow([('1', 'VSL'), ('2', 'Application'), ('3', 'Booked call')], name='p2_flow_clover.png')

# ================= 2.5 TEAM =================
h1('Team, SOPs And Hiring Editors', stat='Minimum 2 editors')
bullets([
    'I always have at least two editors, especially when posting daily. With one, they burn out.',
    'With two or three on hand they compete on quality.',
    'Inayah McMillan\'s only jobs in the process: approve ideas and record scripts. I didn\'t get on a call with her for the first two months. I worked with her operator.',
])

h2('Where To Find Editors')
bullets([
    'All of mine come from Twitter.',
    ('Editors follow editors', ['Find one editor who posts editing content.', 'Look at who follows him: other editors.', 'One becomes two, two become four.']),
    'You don\'t need followers. Editors reply to anyone, as long as you clearly aren\'t a bot.',
])

h2('The Hiring Funnel')
flow([('1', 'Post on socials'), ('2', 'Google form'), ('3', 'Same trial task'), ('4', 'Hire + refine')], name='p2_flow_hiring.png')
stack([
    ('Google form', 'founder story + social links'),
    ('Rabbit line', '"If you are reading this, type rabbit"'),
    ('Trial task', 'same base task for everyone'),
], title='Filters')
bullets([
    ('Application form', ['Fewer applications, higher quality.', 'About 50% of applicants miss the rabbit line. Don\'t give them the benefit of the doubt.']),
    ('Trial task', ['Short form: a 30-second edit.', 'You\'re looking for someone you can refine who is already 90% there.', 'My default is a free trial task. A paid one works too, like 10 thumbnail editors at $50 each. If someone won\'t do a free trial task, they\'re probably not good enough.']),
    'I once hired someone my gut said no to. It was a nightmare and cost more than not hiring.',
])

h2('What It Costs')
bullets([
    'Pay $10 to $100 and you\'ll wonder why the video isn\'t good.',
    'The lower the price, the more you manage them. I pay a premium so I manage less. Editing isn\'t my strongest skill.',
    'Today an agency runs my editing. They hire and fire. If an editor doesn\'t respond within 24 hours, the video goes to someone else.',
])

h2('Reviewing And Briefing')
bullets([
    'New editor: they edit the first 2 minutes only. I comment. Once those are good, they edit the rest.',
    'I check that the visuals expand on what I\'m saying. If I mention it, show it.',
    'Clarity test: can you see what you\'re looking at on first glance.',
    'Give a full brief with every piece of information.',
    'I once left almost 100 comments on a 17-minute edit.',
    'Feedback goes into the next video. No endless re-edits.',
])

h2('The Editing SOP')
label('Client:', 'Chamath Palihapitiya · we edit his channel')
img('p2_chamath_popular.jpg', 6.5, caption='(Chamath\'s channel, Popular tab.)')
img('p2_chamath_text_cards.jpg', 6.5, caption='(His house style: plain text cards over moody B-roll.)')
bullets([
    'His team gave clear input on what they wanted. Our job was to bring it to life without anything flashy getting in the way of what he says.',
    'The goal: same quality at volume, with minimal corrections from his team.',
    ('Short-form SOP we hand editors', ['File naming', 'Safe zone', 'One plain font', '30-second self-check before hand-off']),
])

h2('Mistake We See: The Founder Re-Editing Every Cut')
para('The bottleneck was never the edit. It was always the script. I spend 5 hours on my script so I save 40 hours for my editor.')
