# LM7: Recording equipment guide (v1, 2026-10-06). Rebuilds the old Gamma "Subscribr-Recording-Equipment.pdf".
# Build: python3 ~/.claude/skills/lead-magnet-doc/scripts/docbuilder.py content.py "The Only Setup Guide You Need For Recording YouTube Videos.docx" --img-dir img
AMZ = 'https://www.amazon.com/dp/'
def buy(asin, label='Amazon'):
    return f'[[{label}|{AMZ}{asin}]]'

title_page('The Only Setup Guide You Need For Recording YouTube Videos',
           [('The Gear To Buy At Every Budget, And ', False), ('Exactly', True), (' How To Set It Up', False)], hero='hero.jpg')
toc_page()

# ================= TL;DR =================
h1('TL;DR')
para("I'll be honest with you. I'm not a camera guy. I'm a script guy. But I've filmed enough videos, and helped enough business owners film theirs, to know which gear is worth the money and which is a waste.")
para("The whole doc in five lines:")
bullets(["Pick one of the three setups below, buy it once, and stop watching gear reviews.",
         "The light on your face matters more than the camera you shoot on.",
         "Pull your desk away from the wall. That one move makes a cheap camera look expensive.",
         "Record your screen with Tella, not OBS. It crashes way less.",
         "Hate all of this? Rent a studio for $100 to $200 an hour and walk in with nothing but your script."])
para("If you already know you don't want to set anything up at home, skip straight to the section called **Don't Want To Set Anything Up? Rent A Studio.**")

# ================= WHO WE ARE =================
h1('Who We Are')
para("My name is Bryan, and I run Viral Bangers. We're a YouTube agency for business owners who sell something, like coaches, traders, consultants and info product businesses. We handle the ideas, the scripts, the editing and the thumbnails, so all you have to do is show up and record.")
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
para("Every one of them had to figure out the same thing you're figuring out right now: what do I actually film this on?")

# ================= WHY =================
h1('Why Your Setup Matters')
para("When someone lands on your video, they decide in the first few seconds if you look like someone worth listening to. Bad sound or a dark, grainy face reads as \"amateur\", and if you sell a service, amateur costs you leads.")
para("The good news is that you only buy this stuff once. The same camera, light and mic will film every video you make for the next one to five years. And the better your raw footage is, the more your editor can do with it.")
para("Now, you might be thinking: \"Bryan, which setup is the best one?\"")
para("There isn't one. Every creator will tell you their gear is the best, and you can lose weeks going down that rabbit hole. Pick a setup that fits your budget, learn it, and get a little better every video. Your first video doesn't need to look like a Netflix show.")
para("**Try this:** before you read on, decide which budget you're working with. Under $200, around $2,500, or $8,000 and up.")

# ================= PICK =================
h1('Pick Your Budget')
para("Here are the three setups side by side. Every product in this doc has an Amazon link next to it, and the prices are what they cost in October 2026, so check them before you buy.")
table([['', 'Beginner', 'MVP', 'Premium'],
       ['Total', 'About $130', 'About $2,400', 'About $8,300'],
       ['Camera', 'Your iPhone', 'Sony ZV-E10 II', 'Sony FX3 + ZV-E10 II'],
       ['Light', 'Ring light', 'Elgato Key Light', 'amaran 60d S + softbox'],
       ['Mic', 'DJI Mic Mini', 'Shure MV7+', 'Shure SM7B'],
       ['Teleprompter', 'Free app', 'Elgato Prompter', 'Elgato Prompter'],
       ['Best for', 'Your first 10 videos', 'Posting every week', 'A dedicated studio room']],
      [1.3, 1.7, 1.75, 1.75])
para("If you're not sure, start with Beginner. You can always upgrade later, and you'll know what you actually need by then.")

# ================= BEGINNER =================
h1('Beginner Setup: Start With Your iPhone')
para("My first video took me 5 hours to film 10 minutes of footage. It got 20,000 views and brought in my first paying clients. I shot it on an iPhone.")
para("So don't let gear be the reason you haven't started. Your phone already shoots 4K. What it needs is something to hold it still, some light, and a mic that isn't across the room.")
img('beginner_kit.jpg', 6.5)
table([['What', 'Pick', 'Price', 'Link'],
       ['Tripod', 'UBeesize 67" phone tripod with remote', '~$30', buy('B08CHFY4R5')],
       ['Light', 'UBeesize 10" ring light with stand', '~$30', buy('B0H4GK41PT')],
       ['Mic', 'DJI Mic Mini (with phone receiver)', '~$55 to $99', buy('B0FQJH54TR')],
       ['Teleprompter', 'Any free teleprompter app', '$0', 'App Store']],
      [1.2, 2.8, 1.1, 1.4])
img('ringlight_use.jpg', 6.0, caption='(Your phone sits in the middle of the ring, so the light hits your face straight on.)')
para("No budget at all? Sit facing a window during the day. The window is your light, and it's free.")
img('diag_beginner.jpg', 6.0)
h2('Set Up Your iPhone')
bullets(["Go to Settings, then Camera, then Record Video, and pick 4K at 30 fps.",
         "Use the back camera, not the selfie camera. It's a lot sharper.",
         "Turn the phone sideways (landscape) for long-form videos.",
         "Wipe the lens with your shirt. You'd be surprised how often this is the problem.",
         "Tap and hold on your face before you hit record to lock the focus and brightness.",
         "Turn on airplane mode so a phone call doesn't wreck your take.",
         "Make sure you have at least 20 GB free. 4K eats storage fast."], numbered=True)
h2('Connect Your Mic')
img('mic_clip.jpg', 6.0, caption='(Clip it to your collar or shirt, about a fist below your chin.)')
bullets(["Plug the DJI receiver into the bottom of your iPhone. On an older Lightning iPhone, you'll need a Lightning adapter.",
         "Turn on the transmitter and clip it to your shirt, about a fist below your chin.",
         "Open the Camera app and record 10 seconds of yourself talking.",
         "Play it back with headphones on. If you sound close and clear, the phone is using the mic. If you sound far away and echoey, it isn't, so unplug it and try again."], numbered=True)
para("**Try this:** film a 60-second test this week. It doesn't need to be a real video. Watch it back on your phone and write down one thing to fix.")

# ================= MVP =================
h1('MVP Setup: What I Recommend')
para("This is the setup I'd tell most of our clients to buy. It's the jump from \"filmed on a phone\" to \"this person is a professional\", without paying for a cinema camera.")
img('mvp_kit.jpg', 6.5)
h2('Camera')
table([['What', 'Pick', 'Price', 'Link'],
       ['Camera', 'Sony ZV-E10 II (body only)', '~$950', buy('B0D92W8GYV')],
       ['Lens', 'Sigma 16mm f/1.4 (Sony E mount)', '~$370', buy('B077BWD2BB')],
       ['Memory card', 'SanDisk Extreme 128GB', '~$35', buy('B09X7DZ9LG')],
       ['Power', 'NP-FZ100 dummy battery + wall adapter', '~$50', buy('B091YJBXM4')],
       ['Tripod', 'ULANZI F38 travel tripod', '~$150', buy('B0BXD5YJC5')]],
      [1.2, 2.8, 1.1, 1.4])
para("The ZV-E10 II is the newer version of the camera I filmed on. It's made for people who talk to a camera, so the autofocus stays locked on your face. The Sigma lens lets in a lot of light and blurs your background, which is half of that \"expensive\" look.")
para("The dummy battery plugs into the wall so the camera never dies mid-take. The new ZV-E10 II uses the bigger NP-FZ100 battery, so make sure you buy the FZ100 version, not the old one.")
img('zve_flip.jpg', 4.5, caption='(The screen flips round to face you, so you can check your framing before you hit record.)')
h2('Light: Elgato Key Light')
img('keylight.jpg', 5.0)
table([['What', 'Pick', 'Price', 'Link'],
       ['Main light', 'Elgato Key Light', '~$180', buy('B07L755X9G')],
       ['Smaller option', 'Elgato Key Light Air MK.2', '~$120 to $140', buy('B0GYDFGCCQ')]],
      [1.2, 2.8, 1.1, 1.4])
para("The Key Light is a big, flat panel that clamps to your desk. Because the panel is wide, the light comes out soft, so you don't get harsh shadows on your face. You control the brightness and colour from your computer or phone. If your desk is small, get the Key Light Air instead.")
img('keylight_use.jpg', 6.0, caption='(It clamps to the back of your desk. Raise the panel above your eyes and point it down at your face.)')
h2('Microphone')
table([['What', 'Pick', 'Price', 'Link'],
       ['Mic', 'Shure MV7+ (USB-C)', '~$280', buy('B0CTJ7PVN1')],
       ['Boom arm', 'RØDE PSA1+', '~$99', buy('B09JBVR5B4')]],
      [1.2, 2.8, 1.1, 1.4])
para("The MV7+ plugs into your computer with one cable. No audio interface, no extra boxes. It sounds close to the SM7B in the Premium setup for a lot less hassle.")
img('boom_desk.jpg', 4.0, caption='(A boom arm keeps the mic close to your mouth and off your desk.)')
h2('Teleprompter')
table([['What', 'Pick', 'Price', 'Link'],
       ['Teleprompter', 'Elgato Prompter', '~$200 to $250', buy('B0CH3P9K1X')]],
      [1.2, 2.8, 1.1, 1.4])
para("This sits over your camera lens and shows your script, so you can read it while looking straight down the lens. It's honestly one of the best things I've bought for filming. It's saved me hundreds of hours of trying to memorise lines and redoing takes.")
img('prompter_use.jpg', 6.0, caption='(The script shows on glass right in front of the lens, so you look straight at the viewer while you read.)')

# ================= PREMIUM =================
h1('Premium Setup: The Studio Look')
para("This is for when YouTube is a real part of your business and you have a room you can leave set up. Two cameras, a proper studio light, and the mic you see on every podcast.")
img('premium_kit.jpg', 6.5)
table([['What', 'Pick', 'Price', 'Link'],
       ['Main camera', 'Sony FX3 (now sold as the FX3A)', '~$4,298', buy('B0F7RXXGH1')],
       ['Lens', 'Sony FE 24mm f/1.4 GM', '~$1,300', buy('B07HJXVHSS')],
       ['Second camera', 'Sony ZV-E10 II + Sigma 16mm', '~$1,320', buy('B0D92W8GYV')],
       ['Key light', 'amaran 60d S', '~$140', buy('B09QW9GLL6')],
       ['Softbox', 'amaran Light Dome Mini SE', '~$69', buy('B0BVVTG2ZF')],
       ['Light stand', 'NEEWER C-stand with boom arm', '~$100', buy('B07D8WF443')],
       ['Fill light', 'Elgato Key Light', '~$180', buy('B07L755X9G')],
       ['Mic', 'Shure SM7B', '~$399', buy('B0002E4Z8M')],
       ['Audio interface', 'Elgato Wave XLR MK.2', '~$170', buy('B0GGYXY67H')],
       ['Boom arm', 'RØDE PSA1+', '~$99', buy('B09JBVR5B4')],
       ['Mic cable', 'XLR cable, 10 ft', '~$10', buy('B01JNLUA5G')],
       ['Teleprompter', 'Elgato Prompter', '~$200 to $250', buy('B0CH3P9K1X')]],
      [1.4, 2.6, 1.1, 1.4])
para("The FX3 is a cinema camera in a small body. Sony replaced it with the FX3A, which is the same camera and the same picture with a few small updates, so buy whichever one is in stock.")
para("The ZV-E10 II becomes your second angle. Put it off to the side, and your editor can cut between the two shots so the video never feels static.")
para("The amaran 60d S is the light most studios use. It's much brighter than a desk panel, and the dome softbox in front of it spreads the light out so it's soft on your face. The Key Light from the MVP setup moves to the other side as a fill light.")
img('dome_use.jpg', 6.0, caption='(The dome clips onto the front of the amaran and turns a small, harsh light into a big, soft one.)')
para("The SM7B needs an audio interface to work, which is what the Wave XLR is for. If you want to set it up properly, [[this video|https://www.youtube.com/watch?v=KyC-o7PA8BI]] walks through it step by step.")
img('flow_sm7b.jpg', 6.5)

# ================= STUDIO =================
h1('How To Set Up Your Studio')
para("This works for every budget. Same steps whether you're on an iPhone or an FX3.")
img('studio_wide.jpg', 6.5, caption='(One of my setups: desk off the wall, lamps and plants behind, light off to the side.)')
h2('Step 1: Pick A Quiet Room With Soft Stuff In It')
para("Bare walls and hard floors make your voice echo. A room with a rug, curtains, a couch or a bookshelf will sound a lot better before you've bought anything.")
h2('Step 2: Pull Your Desk Away From The Wall')
para("This is the one most people miss. If you sit right up against the wall, the shot looks flat, like a passport photo. Sit 4 to 6 feet in front of it. That space lets the background go soft and blurry, and it gives the shot depth.")
img('then_now.jpg', 6.5, caption='(Left: sitting close to a plain wall. Right: space behind me, so the background blurs.)')
img('diag_room_side.jpg', 6.0, caption='(Wall, then 4 to 6 feet of space, then you, then the camera at eye level.)')
h2('Step 3: Put The Camera At Eye Level And Sit In The Middle')
para("Two rules. Your eyes should sit on the top third of the frame, and you should be dead centre. Camera lens level with your eyes, not looking up your nose and not looking down on you.")
img('thirds.jpg', 6.0, caption='(Eyes on the red line. Body in the middle box.)')
h2('Step 4: Add Two Or Three Things Behind You')
para("A plant, a shelf, a book or something to do with your business. That's enough. Keep it simple for the first few videos, and change one thing at a time as you go.")
h2('Step 5: Put A Lamp Behind You')
para("A small lamp or LED tube somewhere behind you, off to one side. It lights up the background a bit and puts a little glow on your hair and shoulders, so you don't blend into the wall.")
img('plants.jpg', 6.0, caption='(Backlit plants and a warm lamp behind me. That glow is what separates you from the background.)')
h2('Step 6: Set Up Your Soft Light')
para("This gets its own section below, because it's the step that matters most.")
h2('Step 7: Film A Test And Watch It On Your Phone')
para("Record 30 seconds, then watch it on your phone, because that's where most people will see it. Fix the one thing that bugs you most, and film again.")
para("If you want to see someone build a full studio from scratch, [[this Think Media video|https://www.youtube.com/watch?v=EFPi_pJMK7g]] is a good walkthrough.")

# ================= SOFT LIGHT =================
h1('How To Set Up Your Soft Light')
para("Lighting is the difference between people thinking you look fine and people thinking you look great. And the only light you really have to get right is the light on your face.")
para("You want soft light. Hard light, like a bare bulb or the sun at noon, gives you sharp shadows and makes every bit of skin texture stand out. Soft light wraps around your face and looks natural. The bigger the light source is compared with your face, the softer it gets.")
h2('Step 1: Use A Big Light Source')
para("A softbox, a dome or a panel like the Key Light. On the Beginner setup, the ring light works, and so does a big window.")
h2('Step 2: Raise It A Little Above Your Eyes')
para("Put the middle of the light slightly higher than your eyes and tilt it down toward you. Light from above looks natural, because that's where the sun is.")
img('diag_light_side.jpg', 6.0)
h2('Step 3: Move It 45 Degrees To One Side')
para("Don't put it straight in front of you. That makes your face look flat. Move it off to the side, about halfway between the camera and your shoulder. One side of your face will be a little darker, and that's what gives it shape.")
img('light_diagram.jpg', 6.0)
h2('Step 4: Bring It In Close')
para("Get it as close as you can without it showing up in the shot, usually 2 to 3 feet from your face. Closer means softer.")
h2('Step 5: Set The Colour To 5600K')
para("Most lights let you pick a colour, measured in Kelvin (K). 5600K is daylight. Set your light to 5600 and set your camera's white balance to match.")
h2('Step 6: Turn Off The Ceiling Lights')
para("Ceiling lights are a different colour and they come from straight above, which puts shadows under your eyes. Turn them off and let your soft light and your background lamp do the work.")
h2('Step 7: Adjust The Brightness And Check Your Face')
para("Turn the light up until your face is bright but not shiny. Then look at the shadow side. You want it a little darker, not black. If it's too dark, turn the Key Light (or a white wall) on that side up a little to fill it in.")
para("**Try this:** set it up, film 10 seconds, then move the light 1 foot and film again. Compare them side by side on your phone.")

# ================= MIC =================
h1('How To Set Up Your Microphone')
para("People will watch a video that looks a bit rough. They won't watch one that sounds bad.")
bullets(["Keep the mic close. About a hand's width from your mouth, 4 to 6 inches.",
         "Put it slightly off to the side and point it at your mouth, so it doesn't block your face.",
         "Use a boom arm so the mic floats in and out of the shot instead of sitting on the desk.",
         "Wear headphones for the first test and listen for echo, hum or an air conditioner. Turn off anything you can hear."], numbered=True)
img('diag_mic.jpg', 6.0)
img('bryan_mic.jpg', 6.0, caption='(My setup: the boom arm comes in from the side, and the mic sits just below my chin.)')
para("On the Beginner setup, the clip-on DJI mic does all of this for you. Just clip it on your shirt, a fist below your chin.")

# ================= SCREEN =================
h1('How To Record Your Screen')
para("If you teach anything, you're going to want to share your screen at some point. Walking someone through your process on screen is one of the fastest ways to show you actually know what you're doing.")
h2('Use Tella')
para("We use [[Tella|https://www.tella.com]] for screen recordings instead of OBS or Loom. It's just more reliable. OBS crashes, and when your computer runs out of storage halfway through a recording, the file can get corrupted and you lose the whole take.")
para("Tella saves the recording on your computer first and then uploads it, so if something goes wrong there's still a copy. The newest version also warns you before your disk fills up, and stops safely instead of crashing. It puts your camera in a little bubble over your screen, and it exports in 4K.")
para("It costs $13 a month on the Pro plan (paid yearly), and there's a 7-day free trial.")
img('tella_start.jpg', 6.0, caption='(Tella asks how you want to record: screen, camera, or both.)')
h2('How To Download Tella On A Mac')
bullets(["Go to [[tella.com/mac|https://www.tella.com/mac]] and download the app. You need macOS 13 (Ventura) or newer.",
         "Drag Tella into your Applications folder, open it and sign in.",
         "When your Mac asks, allow Screen Recording, Camera and Microphone in System Settings.",
         "Pick screen and camera, choose your mic, and hit record. You get a 3-second countdown.",
         "Hit stop. The video uploads in the background and opens in the Tella editor."], numbered=True)
h2('How To Download Tella On Windows')
bullets(["Sign in at [[tella.com|https://www.tella.com]], click Record and choose Tella for Windows. You need Windows 10 (version 2004) or Windows 11.",
         "Run the installer and sign in with the same account.",
         "In the app settings, turn the quality up to Very High (4K). It starts on a lower setting.",
         "Pick screen and camera, and choose a mic. If your camera is on, you have to choose a mic or it won't record.",
         "Hit the red record button, and hit stop when you're done."], numbered=True)
img('tella_recording.jpg', 6.0, caption='(Recording in Tella with the camera on.)')
para("If you want to use your Sony as the camera inside Tella instead of your webcam, you'll need an [[Elgato Cam Link 4K|https://www.amazon.com/dp/B07K3FN5MR]] (~$80 to $130) and a [[micro HDMI to HDMI cable|https://www.amazon.com/dp/B07KSDB25X]] (~$8). The cable goes from the camera into the Cam Link, and the Cam Link plugs into your computer, so it shows up like a webcam.")
img('flow_camlink.jpg', 6.5)
h2('Still Using OBS? Use These Settings')
para("If you're sticking with OBS, these settings will save you most of the headaches:")
bullets(["Recording format: Hybrid MP4. Never plain MP4, because if OBS crashes you can't recover the file.",
         "Resolution: 1920x1080 for both Base and Output.",
         "Frame rate: 30, or 60 if you scroll and move around a lot on screen.",
         "Audio: 48 kHz.",
         "Keep at least 50 GB free before you hit record. OBS doesn't stop when your disk fills up. It just breaks the file."])
img('obs_056.jpg', 5.5, caption='(Output settings)')
img('obs_057.jpg', 5.5, caption='(Audio settings)')
img('obs_058.jpg', 5.5, caption='(Video settings)')

# ================= SONY SETTINGS =================
h1('Sony Camera Settings Cheat Sheet')
para("For the MVP and Premium setups. Set these once and you won't have to touch them again. If you'd rather watch someone do it, [[this tutorial|https://www.youtube.com/watch?v=jH3lSgzMNPA]] goes through it on the ZV-E10.")
bullets(["Switch to video mode and pick manual (M) mode.",
         "File format: XAVC S 4K.",
         "Record setting: 24p 100M. (30p 100M is fine too.)",
         "Shutter speed: 1/50 for 24 fps, or 1/60 for 30 fps. The rule is double your frame rate.",
         "Aperture: the lowest number your lens goes to (f/1.4 on the Sigma). Lower number, blurrier background.",
         "ISO: start at 100 and only raise it until the exposure meter reads 0. If you need to go above 800, add more light instead.",
         "White balance: set it to 5600K so it matches your light.",
         "Focus area: Wide. Focus mode: Continuous AF.",
         "Turn on Face/Eye AF and the face frame display, so you can see it's tracking you.",
         "If your mic plugs into the camera, set the audio level so your loudest words peak around -12 dB."], numbered=True)

# ================= STUDIO RENTAL =================
h1("Don't Want To Set Anything Up? Rent A Studio")
para("Honestly, this is what I'd do if I were starting again.")
para("When I moved to Medellín, recording studios there were $20 an hour. That's really cheap, and you won't find that in most cities. But even at normal prices, renting a studio is a great option, for two reasons.")
para("First, everything is already there. Camera, lights, mic, sometimes a teleprompter and someone to press record. You don't stress about any of it.")
para("Second, it forces you to actually record. When you've paid for 3 hours on a Tuesday, you show up with your scripts ready. At home, \"I'll film it tomorrow\" turns into next month. I book a studio, batch a bunch of videos in one sitting, and I'm done for weeks. I explain how in [[this video|https://www.youtube.com/watch?v=4JR47fUrz88]].")
h2('How Much Should You Pay?')
para("In most cities, expect to pay **$100 to $200 an hour** for a studio with the cameras, lights and mic included. That's the range I'd look in. Bare rooms with no gear can be cheaper, and studios that include a producer or a full crew can go well above $300 an hour.")
para("Before you book, check five things:")
checklist(['The price per hour, and the minimum number of hours',
           'Which cameras, lights and mics are included',
           'Whether they have a teleprompter',
           'Whether someone is there to run the camera, or if it\'s self-serve',
           'How you get your footage at the end (USB drive, Google Drive link, same day or next day)'])
h2('Find Studios Near You With Claude Cowork')
para("This is how I find studios now. Instead of calling around for an afternoon, I get Claude to do it and hand me a spreadsheet.")
bullets(["Open the Claude desktop app and go to the Cowork tab.",
         "Copy the prompt below and paste it in.",
         "Replace the part in brackets with your exact address or neighbourhood and city. The more exact, the better the distances.",
         "Let it run. It'll search, open each studio's site and build the sheet.",
         "Open the Top 5 tab, and send the message it writes for you to each one."], numbered=True)
table([['Copy and paste this into Claude Cowork'],
       ["OBJECTIVE\n"
        "Find every recording studio near [YOUR EXACT ADDRESS OR NEIGHBOURHOOD, CITY] that I could book in the next 7 days to film talking-head YouTube videos, and put them all in one Excel sheet so I can contact them today.\n\n"
        "OUTPUT SCHEMA\n"
        "Create an Excel file called \"Recording Studios - [CITY].xlsx\" with one row per studio and these columns: Studio Name, Address, Distance From Me, Price Per Hour (USD), Minimum Hours, Day Rate (if listed), Available In The Next 7 Days (Yes / No / Unknown, plus the open dates), Rooms (list each room or set), Cameras Included, Lights Included, Microphones Included, Teleprompter (Yes / No), Operator Or Videographer Included (Yes / No, and the extra cost), Phone, Email, WhatsApp or Instagram, Booking Link, Google Rating (stars and number of reviews), Notes.\n"
        "Sort the sheet by price per hour, cheapest first.\n"
        "Add a second tab called \"Top 5\" with the 5 best options for one person filming 2 to 4 hours of talking-head video, with one line on why for each.\n"
        "Add a third tab called \"Messages\" with a short, friendly message I can send each Top 5 studio asking if they have 3 hours free this week for solo talking-head filming, what gear is included, and the total price.\n\n"
        "METHODS (use all of these)\n"
        "1. Search Google Maps for \"recording studio\", \"podcast studio\", \"video studio\" and \"content creator studio\" near my location.\n"
        "2. Search Peerspace, Giggster and Tagvenue for podcast and video studios in my city.\n"
        "3. Open each studio's website and booking page. Pull the prices, the rooms, the equipment list and the booking calendar.\n"
        "4. Check each studio's Instagram and Google Business profile for a phone number, email and WhatsApp.\n"
        "5. If availability isn't shown online, write \"Unknown, ask\".\n"
        "6. Skip music-only studios unless they list video cameras and lights.\n\n"
        "RULES\n"
        "Only include real studios you found a source for, and put the source link in Notes. Never guess a phone number or an email. If something isn't listed, leave the cell blank."]],
      [6.5])
h2('Or Hire A Videographer')
para("If you'd rather film at your office or at home and not think about any of the gear, hire a videographer for the day. I've paid $500 for a full day, and that's pretty typical.")
para("When you book one, ask for three things: the raw files (not just an edited video), two camera angles, and a proper mic on you, not just the camera's built-in one. Then show up with your scripts written, and film as many videos as you can in that one day.")

# ================= CHECKLIST =================
h1('Your Record This Week Checklist')
para("Go through this before you film your next video:")
checklist(['I picked one setup and bought it (or I booked a studio)',
           'My desk is 4 to 6 feet away from the wall',
           'The camera is at eye level, and my eyes are on the top third of the frame',
           'I have 2 or 3 things behind me and a lamp off to one side',
           'My soft light is a little above my eyes, 45 degrees to the side and 2 to 3 feet away',
           'My light and camera are both set to 5600K, and the ceiling lights are off',
           'My mic is 4 to 6 inches from my mouth',
           'I filmed a test and watched it back on my phone',
           'Tella is installed for screen recordings'])

# ================= CTA =================
h1('Want Us To Do This For You?')
para("Gear is the easy part. What actually grows your business on YouTube is what you say once the camera's rolling: the ideas, the scripts, the editing and the thumbnails. That's what we do at Viral Bangers. You show up and record, and we handle the rest.")
cta_link('viralbangers.com', 'https://viralbangers.com')
