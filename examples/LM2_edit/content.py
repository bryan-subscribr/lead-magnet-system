# LM2 EDIT lead magnet: "How To Edit YouTube Videos Using Claude (Full Guide)", built from Mauricio Mozo's video xn3IKXrPHvw.
# Voice: Mauricio (co-founder, Viral Bangers). Images in ./img (frames pulled from the video).
VID = 'https://www.youtube.com/watch?v=xn3IKXrPHvw'
def at(t, label=None):
    m, s = divmod(t, 60)
    return f'[[{label or f"{m}:{s:02d}"}|{VID}&t={t}s]]'

title_page('How To Edit YouTube Videos Using Claude (Full Guide)',
           [('Step By Step, With ', False), ('Every', True), (' Prompt I Use', False)], hero='hero.jpg')
toc_page(levels=1)

# ================= TL;DR =================
h1('TL;DR')
para("Hey, I'm Mauricio, co-founder of Viral Bangers. Editing is my whole world. My team and I have edited over 1,500 long-form YouTube videos, and a few weeks ago I got obsessed with editing using AI.")
para("This guide is the written version of my full tutorial. It shows you how to take a raw talking head recording and turn it into an edited, animated video using Claude, even if you've never edited a video in your life. Every prompt I typed is in here so you can copy it.")
img('video_thumb.jpg', 5.5, caption='(The full video this guide is based on.)')
para(f"**Watch it here:** {at(0, 'How To Edit YouTube Videos Using Claude (Full Guide)')}. Every section below also links to the exact moment in the video, so you can watch me do it while you read.")
para("Here's the whole process in one breath:")
bullets(["Set up Claude Code and a free animation tool called HyperFrames (about 15 minutes).",
         "Step 1: give Claude videos you like and have it break down every animation, frame by frame.",
         "Step 2: tell Claude to build animations the way a real editor would, with depth, easing and momentum.",
         "Step 3: save everything that worked as a reusable system, so your next video starts on-brand.",
         "Then cut the footage, add emphasis text, transitions and sound, and export."], numbered=True)
para("**Before you get excited, here's the honest part.** You need a computer (not a phone), a Claude subscription, and some patience. Your first animation will take an hour or two. By your fifth video it gets fast, because you're reusing templates instead of starting from zero.")
para("And if you run a business, you don't need Hollywood. You need three or four animations you reuse in every video: a roadmap in the hook, your process, and a before and after number. I'll show you exactly how to get those near the end.")

# ================= WHO WE ARE =================
h1('Who We Are')
para("Viral Bangers is a YouTube agency for business owners who sell something, like consultants, coaches, traders and info product businesses. I run it with my co-founder Bryan. We handle the ideas, the scripts, the editing and the thumbnails, so all you have to do is show up and record. Bryan and I also run the Creator Room events in Medellín together.")
para("My side is editing. My team produces over 100 videos every month, and we've passed 1,500 long-form videos for some of the biggest personal brands on YouTube.")
img('proof_1500.jpg', 6.0, caption='(Some of the long-form videos my team has edited.)')
para("Here are a few of the people we've worked with:")
bullets(["Chamath Palihapitiya: we edit all of his long-form videos.",
         "Jordan Welch: we scripted \"getting rich is easy, actually\", which has 923,571 views.",
         "Inayah McMillan: our very first video together did 1,185,797 views.",
         "Ethan Garland: we worked on two of his top three videos, including one with 539,000 views.",
         "Scott Taylor: his views went from about 3,600 a video to 15,000, and YouTube now brings in around $40,000 a month.",
         "Fiction Profits Academy: 7,000 to 15,000 subscribers, and they're the top result for \"how to start a KDP business\".",
         "Clover Trading: average views went from about 1,000 a video to 8,000."])
img('clients.jpg', 6.5)
img('clients2.jpg', 6.5)
para("Everything in this guide is how I actually use AI inside the agency. Nothing is held back.")

# ================= WORDS =================
h1('Words You Need To Know (Quick Glossary)')
para("You'll see these words a lot. Read this once and the rest of the guide gets much easier.")
table([['Word', 'What it means'],
       ['Claude Code', 'The "Code" tab in the Claude desktop app. Claude can install things and work with files on your computer for you. You type in normal English.'],
       ['HyperFrames', 'A free tool from HeyGen. Claude writes the animation as a web page, and HyperFrames turns it into an MP4 video.'],
       ['FFmpeg', 'Free software that cuts and exports video files. Claude uses it in the background.'],
       ['Node', 'Background software HyperFrames needs to run (version 22 or higher). Claude installs it for you.'],
       ['GitHub repo', 'A folder of files someone shares online. You give Claude the link and it downloads it.'],
       ['Opus / Fable', "Claude's smartest models. You pick one from the model menu in the chat box."],
       ['Effort (High)', 'A setting next to the model name. High makes Claude think harder and uses more of your plan.'],
       ['Plan mode', 'Claude writes out a plan and waits for your OK before doing anything.'],
       ['Skill', 'A saved set of instructions Claude reuses every time you ask for that thing.'],
       ['Nano Banana', "Google's image generator (inside the Gemini app). You use it to make the pictures your animations are built from."],
       ['B-roll', 'Any visual that goes over or between shots of you talking.'],
       ['Parallax', 'Layers moving at different speeds, so a flat image feels like it has depth.'],
       ['Easing', 'Movement that speeds up and slows down, instead of one robotic speed.'],
       ['XML file', 'A file that opens your edit inside Premiere Pro, DaVinci Resolve or CapCut.']],
      [1.5, 5.0], bold_rows=(0,))

# ================= COST & TIME =================
h1('What This Costs And How Long It Takes')
para("I'm not going to tell you it's all free, because it isn't.")
table([['Thing', 'Cost', 'Notes'],
       ['Claude subscription', '$200 a month (Max plan)', 'The cheaper plan works, but animation eats your credits fast.'],
       ['HyperFrames, FFmpeg, Node', 'Free', 'Claude installs all of it.'],
       ['Nano Banana (Gemini)', 'Free to start', 'For generating the images inside your animations.'],
       ['Gling (cutting tool)', 'Free credits to start', 'Removes silences, bad takes and filler words.'],
       ['Music and sound effects', 'Varies', 'You need licences. I still do this part by hand.'],
       ['A computer', 'You already have one', 'Rendering runs on your machine. This does not work on a phone.']],
      [1.9, 1.7, 2.9], bold_rows=(0,))
para("Time-wise, plan for about 15 minutes of setup, around an hour for your first big analysis (Claude does the work, you wait), and 10 to 30 minutes per animation while you're learning. The real speed comes after 5 or 6 videos, once your templates are saved.")
para("**One rule for the whole guide:** when something breaks, copy the error and paste it back to Claude with \"fix this\". That solves most problems.")

# ================= VIDEO CHAPTERS =================
h1('Watch Along: Every Chapter In The Video')
para("If you'd rather watch than read, here's where everything is. Click any time to jump straight there.")
table([['Time', 'What happens'],
       [at(90), 'Setup'], [at(220), 'What AI video editing actually is'], [at(330), 'The call with the HyperFrames co-founder'],
       [at(450), 'Step 1: Analysis'], [at(690), 'The analysis prompt'], [at(840), 'Step 2: Layers and depth'],
       [at(960), 'The 3 rules'], [at(1110), 'Parallax animation'], [at(1320), 'Two-scene animation'],
       [at(1500), 'Roadmap animation'], [at(1730), 'Multi-scene animation'], [at(1830), 'Step 3: Saving it as a system'],
       [at(1950), 'Templates and asset library'], [at(2070), 'Cutting the footage'], [at(2190), 'Emphasis text'],
       [at(2240), 'Transitions'], [at(2320), 'Sound design'], [at(2430), 'Export']],
      [1.2, 5.3], bold_rows=(0,))

# ================= SETUP =================
h1('Setup: Install Everything In About 15 Minutes')
para(f"(Watch this part: {at(90)}.) This is the boring part, but you only do it once. If you already have Claude Code and HyperFrames, skip ahead.")
para("**1. Get Claude and open the Code tab.** Download the Claude desktop app, sign in, and click the Code tab at the top. Pick a folder for this project (mine is called \"Claude Video Editing\"). Everything you type below goes into that chat box.")
para("**2. Install FFmpeg.** This is what lets Claude cut and export your videos. Just type:")
para("*Hey, I want you to install Node and FFmpeg for me.*")
img('setup_ffmpeg.jpg', 6.0, caption='(The first prompt. You can literally just ask.)')
para("If you're on a Mac and comfortable with it, the exact command is *brew install node ffmpeg*, but you don't need to know that. Claude does.")
para("**3. Install HyperFrames.** This is the tool that runs every animation in this guide, so don't skip it. Paste this:")
para("*npx skills add heygen-com/hyperframes --all*")
img('setup_hyperframes.jpg', 6.0)
img('hyperframes_logo.jpg', 4.5, caption='(HyperFrames, made by HeyGen. It runs almost every AI animation you see online.)')
para("**4. Check that it worked.** Once it finishes, paste this:")
para("*Show the installed command list after it finishes. It's visual proof the install worked.*")
img('setup_check.jpg', 6.0)
para("This matters more than it looks. If you don't have Node 22 or higher, HyperFrames won't work and you'll waste hours wondering why. If the list shows up, you're good.")
para("**5. Bonus: give Claude HyperFrames' own launch videos.** HeyGen shares the files behind their launch videos on GitHub. Giving these to Claude means it learns from real, professional motion graphics instead of guessing.")
img('setup_repo.jpg', 6.5, caption='(The hyperframes-launches repo on GitHub.)')
para("Paste this:")
para("*https://github.com/heygen-com/hyperframes-launches Please also install this GitHub in your memory of HyperFrames. It contains most of the launches they have done and the editing process they used for the motion graphics.*")
img('setup_repo_prompt.jpg', 6.5)
para("That's it. You're set up.")

# ================= WHAT AI EDITING IS =================
h1('What AI Video Editing Actually Is')
para(f"(Watch: {at(220)}.) Before you start, you need to understand this, or you'll get bad results and blame the tool.")
para("**AI video editing is not one button that turns raw footage into a finished video.** Nobody has cracked that yet, and anyone selling it to you is lying.")
para("What it actually is: turning code into animation. AI is very good at writing code. So instead of asking a machine to imagine a video, you ask it to write code, which is the thing it's trained for. HyperFrames takes that code (a web page made of HTML and CSS) and renders it into an MP4.")
img('html_mp4.jpg', 6.5, caption='(Claude writes the code. HyperFrames turns the HTML into an MP4.)')
para("Why HTML? Because it's one of the oldest languages on the internet. There are decades of examples for the AI to learn from.")
img('hyperframes_docs.jpg', 6.0)
para("This took me weeks to understand: you're not hiring a machine to make a video. You're hiring a fast editor who also happens to code. **The tool doesn't make the video good. You do. You're the editor.** Everything in this guide comes from that.")

# ================= SLOP STORY =================
h1('Why My First Animations Looked Like AI Slop')
para(f"(Watch: {at(330)}.) When this trend started, I figured I had an unfair advantage. I gave Claude everything we use at the agency: overlays, our whole library, even a prompt generator for every scene I wanted.")
para("And I still got AI slop. The same flat, generic stuff you see everywhere.")
img('flat_roadmap.jpg', 6.0, caption='(Clean, but flat. Nothing has depth and nothing feels alive.)')
para("I was about to quit. I even tweeted about hating on HyperFrames. Then one of the co-founders of HyperFrames saw the tweet, saw that I run an editing agency, and invited me on a call.")
img('tweet.jpg', 5.5, caption='(The reply that started it.)')
para("In 15 minutes he gave me three pieces of advice that changed everything. Those three pieces are Steps 1, 2 and 3 below.")

# ================= STEP 1 =================
h1('Step 1: Have Claude Analyse The Videos You Want To Copy')
para(f"(Watch: {at(450)} and the prompt at {at(690)}.) The first thing he told me: the newest Claude models are very good at analysing video, frame by frame. So you don't need any extra tools. People will tell you to set up a notebook or a database first. You don't need any of that.")
para("**1. Pick the right model.** In the chat box, choose Opus 5 or Fable 5 from the model menu, and set the effort to High. Other models can't really analyse a video frame by frame.")
img('opus_high.jpg', 5.0, caption='(Bottom right of the chat box: Opus 5, High.)')
para("**2. Turn on Plan mode.** Plan mode makes Claude plan everything and wait for your OK before it starts. In the Code tab, click the mode button next to the chat box (or press Shift+Tab) until it says Plan.")
img('plan_mode.jpg', 6.0)
para("**3. Write a short brand sheet first.** I already have an editing SOP with my colors, fonts and the channels I like. If you don't, make one before you start. It can be five lines:")
bullets(["My brand colors: [HEX CODES]",
         "My fonts: [HEADING FONT] and [BODY FONT]",
         "Pacing: [fast and punchy / calm and clean]",
         "Channels I want to look like: [3 YOUTUBE CHANNEL LINKS]",
         "My audience: [WHO WATCHES AND WHAT THEY BUY]"])
para("Save it as a file in your project folder and tell Claude to read it. That's what stops every animation from looking like everyone else's.")
para("**4. Pick 3 reference channels.** I picked one in my niche, one in the business niche and one in the personal brand niche.")
img('analysis_channels.jpg', 6.5, caption='(Two of the channels I gave Claude to study.)')
para("Think about how you'd brief a real editor. You wouldn't say \"make it nice\". You'd send references and show them what you want. That's exactly what you're doing here.")
para("**5. Paste the analysis prompt.** Here's the one I used, cleaned up so you can copy it:")
para("*I'm going to give you three YouTube channels that I really like. Using HyperFrames and the GitHub of launch videos you installed during setup, I want you to analyse their videos from the last six months. When I say analyse, I want you to understand frame by frame what happens on screen in the hooks, the first 30 seconds to 1 minute: the animations, the roadmaps, the different scenes, and how they hook viewers visually. List all the resources and tools they use. Also create a B-roll annotation skill: when I give you a video, you transcribe it, and based on what these creators do, you tell me which images to make so you can build an animation. I will create the images with Nano Banana, so give me the prompts. We're optimising for YouTube retention, so every video needs a roadmap in the hook. Be very precise. When you're done, recreate these animations first, before you touch any of my footage. Tell me if you need any resources. Read my brand sheet first: [FILE NAME]. Channels: [CHANNEL 1] [CHANNEL 2] [CHANNEL 3]*")
img('analysis_prompt.jpg', 4.5, caption='(The real prompt as I typed it.)')
para("This one takes about an hour and uses a lot of credits. That's normal. Let it run.")
para("**6. Make the images in Nano Banana.** When Claude gives you image prompts, paste them into Nano Banana (in the Gemini app), download the images, and drop them into a folder in your project. Then tell Claude where they are.")
para("Here's what came out of one prompt plus a Nano Banana image. On the left is the real creator. On the right is what my AI analysis produced.")
img('analysis_result.jpg', 6.5, caption='(Left: the real creator. Right: our version, straight from the analysis.)')
para("Honestly, you could use that in a YouTube video. And you don't have to analyse three full channels every time. You can give Claude one video with exact timestamps, or just a few screenshots, and it'll rebuild that animation in your brand.")
para("**Try this:** find one video in your market with a graphic you love. Copy the link with the timestamp, paste it into Claude with \"analyse this animation and rebuild it with my branding\", and see what comes back.")

# ================= STEP 2 =================
h1('Step 2: Make Claude Think Like An Editor')
para(f"(Watch: {at(840)} and the rules at {at(960)}.) After Step 1 my animations were good, but still a bit flat. That's because the analysis tells Claude *what* happens on screen. It doesn't tell Claude *how* an editor builds it.")
para("A real motion graphic isn't one layer doing one movement. It's a background, a midground and a foreground, and each one has its own life. Everything moves, all the time.")
img('layers.jpg', 6.5, caption='(Split every shot into layers: background, midground, foreground.)')
para("So here are the three rules I now give Claude on every animation.")
img('three_rules.jpg', 5.5)
para("**Rule 1: Depth.** Split the frame into foreground, midground and background. When the camera pushes in, each layer travels at a different speed. The background barely moves, the midground moves a little, and the foreground moves the fastest. If everything moves at the same speed, it's not a camera move. It's a zoom, and it looks cheap.")
para("**Rule 2: Easing.** Nothing moves at one constant speed, and nothing stops dead. Every movement starts soft, speeds up, and slows down at the end.")
img('easing.jpg', 5.0, caption='(Top: linear, robotic. Bottom: eased, natural.)')
para("**Rule 3: Momentum.** Every move starts before the last one finishes. I use about half a second of overlap, so the pieces never fully stop.")
img('momentum.jpg', 5.0, caption='(Every move starts before the last one finishes.)')
para("And two small ones people always miss: nothing ever just appears, and no two things land at the exact same moment.")
img('appears.jpg', 6.5, caption='(Things slide or scale in, and arrive about 90 milliseconds apart.)')
para("You can paste the rules straight into any animation prompt:")
para("*Build this like a professional motion editor. Rule 1, depth: split the frame into foreground, midground and background, and when the camera moves each layer travels at a different speed. Rule 2, easing: never linear, every move eases in and out. Rule 3, momentum: every move starts about half a second before the last one ends. Nothing just appears, and no two things land at the same time.*")
para("On every animation, ask yourself one question: how would a real editor build this, and what layers would they need?")

# ================= EXAMPLE 1 =================
h1('Example 1: A Parallax City Shot')
para(f"(Watch: {at(1110)}.) Now let's put the steps together. Here's the first animation I wanted to copy, a camera move through layers: clouds, men in suits, a city, cars and stacks of money.")
img('parallax_ref.jpg', 6.0, caption='(The reference animation.)')
para("**The prompt.** I gave Claude the video link with the timestamp and described what I saw:")
para("*[VIDEO LINK WITH TIMESTAMP] From second 11 to second 14 there's an animation with a camera movement. There's a background, a movement behind it, and then a city, a lake, a car, stacks of money, clouds and different overlays. I want to generate an animation like this. Please analyse everything in the image and give me the prompts so I can generate every asset separately with Nano Banana. Then make a realistic animation like this one, using my branding.*")
img('parallax_prompt.jpg', 6.0, caption="(Claude pulled the actual frames and measured the camera move before building anything.)")
para("It even worked out by itself that it was a parallax. It took screenshots of every frame and wrote a full breakdown document, layer by layer, with the Nano Banana prompts for each asset.")
img('parallax_analysis.jpg', 6.0, caption="(Claude's layer-by-layer breakdown.)")
para("**The assets.** I generated every asset in Nano Banana and saved them all into one organised folder.")
img('nano_assets.jpg', 6.0, caption='(Every asset saved separately, so they can be reused later.)')
para("**The result.** About 20 minutes later:")
img('parallax_ai.jpg', 6.5)
img('parallax_result.jpg', 6.5, caption='(Left: the reference. Right: ours.)')
para("Pretty close. With a few more minutes of refining I'd use this in a real video. And the only thing I did differently was treat the AI the way an editor works.")

# ================= EXAMPLE 2 =================
h1('Example 2: A Two-Scene Animation')
para(f"(Watch: {at(1320)}.) This one looks simple, but it's actually two scenes, not one parallax. **And my mistake was treating it as one scene.** My first prompt was vague, and the first result made no sense.")
para("Here's the prompt that got me close:")
para("*[VIDEO LINK WITH TIMESTAMP] I want to recreate something like this, using a white background as the reference and the exact style he's using. I really want you to nail the animations, so analyse all the camera movements, and give me the prompts so I can make the images in Nano Banana. Add a blur vignette on top and any overlays that make this super realistic, with very smooth, eased camera movement.*")
img('twoscene_prompt.jpg', 6.0)
para("Claude measured the reference instead of guessing: how long each card stays on screen, when each piece moves.")
img('twoscene_measure.jpg', 6.0, caption='(Claude timing every part of the reference.)')
img('twoscene_result.jpg', 6.5, caption='(Left: the reference. Right: ours.)')
para("Not pixel-perfect, but very good, and it took 10 to 15 minutes with the refining.")
para("**The lesson:** if an animation has more than one scene, say so in the prompt, and ask Claude to build it scene by scene.")

# ================= EXAMPLE 3 =================
h1('Example 3: A Roadmap Animation')
para(f"(Watch: {at(1500)}.) This is the one I'd copy first if you run a business. A roadmap in the hook tells viewers exactly what they're about to get, and it keeps them watching.")
img('roadmap_ref.jpg', 6.5, caption='(The reference: a roadmap graphic in the first 30 seconds.)')
para("This was a complex one, with a lot of detail, and it took about 30 minutes. The prompt:")
para("*[VIDEO LINK WITH TIMESTAMP] I want to build the motion graphics from second 20 to second 30, using everything we know about cameras, depth, separating every scene, and easing. First, analyse all the assets I need to gather so I can give them to you. Once you have the assets, build the animation scene by scene. Then build the transitions at the end, with the camera movements.*")
img('roadmap_prompt.jpg', 6.0)
para("Notice the order: assets first, then scene by scene, then the transitions last. That order is the whole trick for complex animations.")
img('roadmap_result.jpg', 6.5, caption='(In each frame, the top half is the reference and the bottom half is ours.)')
para("It's basically the same. I could add a paper texture and match the font a little better, but it's super good. And I didn't generate a single new image for this one. Claude used the assets already in my library.")

# ================= EXAMPLE 4 =================
h1('Example 4: A Multi-Scene Sequence')
para(f"(Watch: {at(1730)}.) The last one is the hardest: it starts on a desk with text, goes into a roadmap, then a few more scenes, and then the camera pulls out.")
img('multiscene_ref.jpg', 6.0, caption='(The reference video.)')
para("Here's the prompt. The important part is SCENE BY SCENE:")
para("*[VIDEO LINK WITH TIMESTAMP] From second 22 to second 39, are there parts we can copy in terms of motion graphics? Let's build this scene by scene, and then at the end, connect all of it. Use the same structure, camera movement, depth, easing and effects, and let me know if you need assets. Please do all of this without stopping to ask me for permission.*")
img('multiscene_prompt.jpg', 6.0)
para("I also pasted in my own script, so it knew what each scene was about. Then I just said \"go ahead\" whenever it finished one scene, made a few changes, and this was the result.")
img('multiscene_result.jpg', 6.5, caption='(Three scenes from the sequence. Top half: reference. Bottom half: ours.)')
para("A couple of effects, like a blur, weren't perfect yet. That's one more prompt to fix. Within 30 minutes you can copy almost any animation you see on YouTube.")

# ================= STEP 3 =================
h1('Step 3: Save What Worked So You Never Start From Zero')
para(f"(Watch: {at(1830)} and the library at {at(1950)}.) This is the step most people skip. Once you've made an animation you're proud of, you turn it into a system.")
para("At the end of every chat, I paste this:")
para("*Turn this entire chat history into updates to the relevant mm- house skills: every preference I expressed, the styles I approved, what I rejected and why, and any technique that worked. Route each learning to the right skill. Never write into .claude/skills/motion-graphics/ or any other upstream skill, because those get overwritten.*")
img('save_prompt.jpg', 6.0, caption='(The save prompt, with an extra note about this specific animation.)')
para("You can add a line about the specific animation too. For the parallax I added: \"for complex parallax animations, save the structure of analysing every asset layer by layer, and the Nano Banana prompts you gave me.\" Now every time I ask for a parallax, it splits it into layers, asks me for the assets, and remembers what we tweaked.")
para("**One warning.** When HyperFrames updates, it overwrites its own skills. That's why my skills all start with \"mm-\" (my initials). Anything with your own prefix never gets overwritten. Use your initials instead of mine. Claude handles the rest when you paste the prompt.")
img('prefix_rule.jpg', 6.0, caption='(Your own skills get your own prefix, so updates never wipe them.)')
para("**Build a library.** I keep folders of backgrounds, overlays, sound effects, UX elements and templates. Templates are animations I can call by name, like a five-step roadmap. Say the word and Claude already knows what to build.")
img('library.jpg', 6.5, caption='(My asset library: backgrounds, overlays, sound effects and saved templates.)')
para("**Try this:** after your first good animation, paste the save prompt, then open a brand new chat and ask for the same kind of animation. If it comes out on-brand first try, your system is working.")

# ================= CUTS =================
h1('Cutting The Footage')
para(f"(Watch: {at(2070)}.) Now that you have the animation system, the rest of the edit is the easy part. First, the cuts: removing the bad takes, the filler words, the ums and the silences. A normal editor spends around 3 hours on this. With AI it takes minutes.")
para("**The route I recommend: Gling.** It's what I used to cut the video this guide is based on. It has free credits, and it's simple. Drop in your footage, pick your language, and turn on cut silences, cut bad takes and remove filler words.")
img('gling_options.jpg', 4.5, caption='(Gling: tick these three and click Enhance and edit.)')
para("Then export and you have your cut video. Big files take a while (my footage was about 6 GB), but you don't have to do anything.")
para("**The other route: have Claude cut it.** I have a cut skill, so I can say:")
para("*Run the cut on [VIDEO NAME]. At the end, export the XML file so I can open it in DaVinci Resolve and do the color grading myself. The files are on my SSD. This is the script: [LINK].*")
img('claude_cut.jpg', 6.0)
para("To be honest, it can be a fight. I once spent two hours going back and forth and didn't get there. If you're new, use Gling.")

# ================= ASSEMBLY =================
h1('Putting Your Animations Into The Video')
para("Once your footage is cut and your animations are rendered, you have two options:")
bullets(["Let Claude do it. Give it the cut video and the animation files, and tell it where each one goes (for example, \"put the roadmap animation over 0:08 to 0:20\").",
         "Do it yourself. Ask Claude to export everything as an XML file, open it in Premiere Pro, DaVinci Resolve or CapCut, and drag things around there."])
para("If you've never edited before, start with the first one.")

# ================= EMPHASIS TEXT =================
h1('Adding Emphasis Text')
para(f"(Watch: {at(2190)}.) Emphasis text is the big on-screen words next to you when you say something important.")
img('emphasis_example.jpg', 6.0, caption='(Emphasis text next to the speaker.)')
para("Because Claude already analysed your reference channels in Step 1, you can ask it to copy how they do it:")
para("*Please analyse where these creators put text on screen next to the person, and how they use it. Then, with my video [FILE NAME], suggest text I can use, in my branding.*")
img('emphasis_prompt.jpg', 6.0)
para("The results are very good, and it's quick.")

# ================= TRANSITIONS =================
h1('Adding Transitions')
para(f"(Watch: {at(2240)}.) My tip here is that less is more.")
para("**Light leak transitions.** Search YouTube for \"light leak transitions\", download about 10 free ones, and save them in your templates folder.")
img('light_leaks.jpg', 6.0, caption='(Free light leak packs on YouTube.)')
para("Then give Claude this:")
para("*Every time I say \"light leak transition\", use a light leak from my templates folder with the blend mode set to overlay, placed on top of the two clips we want to connect.*")
img('transition_prompt.jpg', 6.0)
para("**Camera move transitions.** If you have two animations, you can ask Claude for a camera movement that connects them.")
para("**Plain cuts.** Honestly, for a talking head video, a normal cut is the most common transition. Use the fancy ones when you go from an animation back to your footage, and leave the rest as plain cuts.")

# ================= SOUND =================
h1('Sound Design (I Still Do This By Hand)')
para(f"(Watch: {at(2320)}.) This is where AI hits a limit. I've given it a whole library of sound effects, but right now it's only good if you pick the music for it. Knowing what good music and good effects are is still a human job, and you need licences. So I do it by hand.")
img('sfx_library.jpg', 6.0, caption='(My sound effects folder.)')
para("Here are the rules we use at the agency:")
bullets(["In the hook, use a cinematic orchestral track.",
         "Change the music section by section (when the hook ends, when section one ends, and so on), so it never gets repetitive.",
         "Only put sound effects on the moments that matter. Not on every camera move.",
         "When the camera moves, add a soft whoosh you can barely hear.",
         "Before you say something important, add a riser."])
img('sound.jpg', 6.5, caption='(Filtering music by genre and tempo, and the final timeline with music changing by section.)')

# ================= EXPORT =================
h1('Exporting Your Finished Video')
para(f"(Watch: {at(2430)}.) You don't need Premiere Pro. Because FFmpeg is installed, you can just tell Claude:")
para("*Export the video in 4K.* (Or HD.)")
para("It renders on your computer, so it takes about as long as normal editing software. If you shoot on an iPhone and want to color grade, ask for an XML file instead and do the color in DaVinci Resolve. I record on my iPhone and color grade every video myself.")
para("And that's a full video, edited with AI.")

# ================= YOUR BUSINESS =================
h1('How To Make This Work For Your Business')
para("Most of the examples above came from creator channels. You don't need a city full of men in suits. Here's how I'd use this if I sold a service.")
para("**Pick your three reference channels from your market.** One competitor or peer, one big business channel, and one personal brand you like the look of. Run Step 1 on them.")
para("**Build just three templates to start.** That's it. Don't try to copy everything.")
table([['Template', 'What it shows', 'Where it goes'],
       ['Roadmap', '"Here are the 3 steps we used to take [CLIENT TYPE] from [BEFORE] to [AFTER]"', 'In the hook, every video'],
       ['Your process', 'Your 4 or 5 steps (for example: audit, plan, build, results), each one sliding in with depth', 'Whenever you explain how you work'],
       ['Before and after number', 'A result counting up from the old number to the new one (leads, revenue, hours saved)', 'When you share a client result']],
      [1.5, 3.2, 1.8], bold_rows=(0,))
para("Build each one once, save it with the Step 3 prompt, and give it a name. After that, every new video is just \"use my roadmap template with these three steps\".")
para("Now, you might be thinking: \"Mauricio, I don't have time to learn all of this.\" That's fair. Start with the roadmap only. One template, used in every hook, already puts you ahead of most business channels.")

# ================= CHECKLIST =================
h1('The Checklist')
checklist(["Claude desktop app installed, Code tab open, project folder chosen",
           "Node and FFmpeg installed",
           "HyperFrames installed and the command list showed up",
           "hyperframes-launches repo saved to Claude's memory",
           "Brand sheet written (colors, fonts, pacing, 3 channels, audience)",
           "Opus 5 or Fable 5 selected, effort set to High, Plan mode on",
           "Analysis prompt run on 3 reference channels (or one video with timestamps)",
           "Nano Banana images made and saved in one folder",
           "The 3 rules (depth, easing, momentum) pasted into every animation prompt",
           "Complex animations built scene by scene, transitions last",
           "Save prompt pasted at the end of every chat, with your own prefix on your skills",
           "Asset library and templates folder set up",
           "Footage cut in Gling (silences, bad takes, filler words)",
           "Animations placed into the video",
           "Emphasis text added",
           "Transitions kept simple: fancy ones only between animations and footage",
           "Music and sound effects added by hand",
           "Exported in HD or 4K (or XML for color grading)"])

# ================= CTA =================
h1('Want Us To Do This For You?')
para("I'm showing you all of this because I want you to build with it. But if you'd rather not spend months learning and testing, my team can edit for your personal brand. We've edited over 1,500 long-form videos, and we can install our editing system into your business.")
cta_link('viralbangers.com', 'https://www.viralbangers.com')
