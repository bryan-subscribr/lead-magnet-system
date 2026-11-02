// Trainings library: one component, two pages.
//   /trainings            (mode "optin")   email-only opt-in → Kit form 10022732 (tag "Trainings Library Opt-in"),
//                                          which starts the "Trainings Library Delivery" sequence, then sends people to /trainings-confirmed.
//   /trainings-confirmed  (mode "library") every training as an alternating thumbnail / headline row, linking straight to the Google Doc.
// Adding a training = one entry in TRAININGS (thumbnail is an image taken from inside that guide's Google Doc).
import { useEffect, useState } from "react"
import { addPropertyControls, ControlType } from "framer"

const FORM = 10022732
const TAG = 24449232
const CONFIRMED = "/trainings-confirmed"
const DOC = "https://docs.google.com/document/d/"
const IMG = "https://framerusercontent.com/images/"

type Training = {
    keyword: string
    doc: string
    thumb: string
    title: string
    mark: string
    sub: string
}

const TRAININGS: Training[] = [
    {
        keyword: "SCRIPT",
        doc: DOC + "1OnxBRiIg-9a8PKmah0Ani9zUF0RS0fGpLmVhh5A1xsk/edit?usp=sharing",
        thumb: IMG + "1IDHsMN60U9F3XmDPvCLxJ1LIM.jpg",
        title: "The Script Behind Jordan Welch's",
        mark: "923,571-View Video",
        sub: "A line-by-line breakdown of the script we wrote for Jordan, so you can write scripts that keep people watching to the end.",
    },
    {
        keyword: "SCOTT",
        doc: DOC + "14JHrz6mIf3rHIYbzqLa_GdaU-cp0jq-zLl1NWMcUI1I/edit?usp=sharing",
        thumb: IMG + "FpJ9rdppaiD9B7010Kf7ui1RqSM.jpg",
        title: "How Scott Taylor Tracks",
        mark: "About $40,000 a Month Back to YouTube",
        sub: "How a channel he thought was dead became his best source of clients, and how he traces every call back to a video.",
    },
    {
        keyword: "MILLION",
        doc: DOC + "1G6gyDiWEyE6oTNBS56qdIFeZ8Fh6ox_41vsOz2TeuN8/edit?usp=sharing",
        thumb: IMG + "XkE9QauDAicvzCAfGEp0Iidxhb4.jpg",
        title: "How We Got Inayah McMillan",
        mark: "1,185,797 Views on One Video",
        sub: "The positioning behind her first video with us, and how to find the angle only you can make.",
    },
    {
        keyword: "THUMBNAILS",
        doc: DOC + "1gz4VoJxQW9mt_qVE0l27R_-AwdxTiEZDQ7w_4YUsf3A/edit?usp=sharing",
        thumb: IMG + "wN2CYcMosD5cwbDoF6N5VZMOvaY.jpg",
        title: "The 6-Part Thumbnail Formula That Gets RP Profits",
        mark: "4.4x the Views",
        sub: "Every part of the formula, shown on the real thumbnails we made for RP Profits, so you can use it on your next video.",
    },
    {
        keyword: "ALGORITHM",
        doc: DOC + "1uKia2GXBI592Nrk6-4wS_m_49b0uG7ifWi3uqPEW5R8/edit?usp=sharing",
        thumb: IMG + "JHA6Q6UjH5Gkim9iuPHTilaHY.jpg",
        title: "The New Rules of",
        mark: "The YouTube Algorithm (for 2027)",
        sub: "How YouTube decides which videos to push now, and what to change on your next upload so it gets pushed instead of buried.",
    },
    {
        keyword: "IDEAS",
        doc: DOC + "1zzV1Vz8aGbl24ftDvYGTMoSuV8sTb4INJ5hE9U-Lak8/edit?usp=sharing",
        thumb: IMG + "d0N1rMVGs2MJiLwkF4ZprnTsU.jpg",
        title: "How To Come Up With BANGER Video Ideas",
        mark: "That Build Your Brand And Get You Sales",
        sub: "The way we pick topics and formats for our clients, so your videos bring in sales, not just views.",
    },
    {
        keyword: "EDIT",
        doc: DOC + "1-qo8fvNmqzGHifdI28FOddSi3QM-QtveNpd82FLQ-BQ/edit?usp=sharing",
        thumb: IMG + "lJ9VK5vohDj6XcNnMlER7NRPY.jpg",
        title: "The Editing Checklist Behind 100M Views",
        mark: "For Business YouTube Channels",
        sub: "The checklist we use when we edit Chamath Palihapitiya's channel, so every video is easier to watch to the end.",
    },
    {
        keyword: "CLAUDE",
        doc: DOC + "1VxLy8Jy2nu7GVoJXXI3lvYyA62j5LmixJq82Dq6FwyA/edit?usp=sharing",
        thumb: IMG + "Dhf7KW0tj5ljFc0Dl0JrZHnsfIM.jpg",
        title: "How To Edit YouTube Videos",
        mark: "Using Claude",
        sub: "My full guide to editing with Claude, with every prompt I use, so you can edit faster with AI.",
    },
    {
        keyword: "SETUP",
        doc: DOC + "1-gyDLFbtP6LnwG2-gsfRMVzYnaAg5UWPiS-0txBdTfU/edit?usp=sharing",
        thumb: IMG + "6q5UD5tkBIPgbnWjIiRIxfuRFKM.jpg",
        title: "The Only Setup Guide You Need",
        mark: "For Recording YouTube Videos",
        sub: "The camera, mic and lighting to buy at three budgets, so you can film at home and look the part.",
    },
]

const CSS = `
.tr{--o:#ED7D37;--y:#FBD357;--c:#FFF2E8;--k:#0A0A0A;--mut:#5E554E;--line:rgba(10,10,10,.12);
font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--k);background:var(--o);width:100%;min-height:100vh;-webkit-font-smoothing:antialiased;container-type:inline-size;container-name:tr;display:flex;flex-direction:column}
.tr *{box-sizing:border-box}
.tr-bar{display:flex;justify-content:center;align-items:center;gap:10px;background:var(--k);color:#fff;padding:13px 16px;font-size:22px;font-weight:700;letter-spacing:-.02em;line-height:1;text-decoration:none}
.tr-bar svg{width:30px;height:30px;flex:none}
.tr-hero{display:flex;flex-direction:column;align-items:center;text-align:center;padding:36px 20px 28px;gap:14px;position:relative;overflow:hidden}
.tr-blob{position:absolute;border-radius:50%;filter:blur(70px);opacity:.45;pointer-events:none}
.tr-hero>*:not(.tr-blob){position:relative}
.tr-tag{display:inline-flex;align-items:center;gap:.4em;background:var(--k);color:#fff;border-radius:999px;padding:9px 18px;font-size:15px;font-weight:600;box-shadow:0 2px 0 rgba(10,10,10,.18)}
.tr-yt{display:inline-flex;align-items:center;gap:.3em}
.tr-yt svg{width:1.35em;height:auto}
.tr h1{margin:6px 0 0;font-size:60px;line-height:1.02;font-weight:700;letter-spacing:-.035em;max-width:920px;text-wrap:balance}
.tr em{font-style:normal;background:linear-gradient(transparent 58%,var(--y) 58%,var(--y) 94%,transparent 94%);-webkit-box-decoration-break:clone;box-decoration-break:clone}
.tr-sub{margin:0;font-size:19px;line-height:1.45;font-weight:500;max-width:640px;text-wrap:pretty}
.tr-card{width:100%;max-width:520px;margin-top:10px;background:#fff;border-radius:20px;padding:20px;box-shadow:0 30px 60px -36px rgba(0,0,0,.55);text-align:left}
.tr-form{display:flex;flex-direction:column;gap:10px}
.tr-form input{width:100%;font:inherit;font-size:16px;padding:15px 16px;border:1px solid var(--line);border-radius:12px;background:var(--c);color:var(--k);outline:none}
.tr-form input:focus{border-color:var(--k);background:#fff}
.tr-btn{appearance:none;border:0;cursor:pointer;width:100%;font:inherit;font-size:17px;font-weight:700;letter-spacing:-.01em;color:#fff;background:var(--k);border-radius:999px;padding:17px 20px;display:inline-flex;justify-content:center;align-items:center;gap:10px;text-decoration:none;transition:transform .2s ease;box-shadow:0 10px 24px -14px rgba(0,0,0,.6)}
.tr-btn:hover{transform:translateY(-1px)}
.tr-btn:disabled{opacity:.6;cursor:wait}
.tr-btn svg{width:18px;height:18px}
.tr-fine{margin:10px 0 0;font-size:12.5px;color:var(--mut);text-align:center;line-height:1.4}
.tr-fine a{color:inherit}
.tr-err{margin:4px 0 0;font-size:14px;color:#B3261E;font-weight:600;text-align:center}
.tr-peek{width:100%;max-width:1080px;margin:0 auto;padding:8px 20px 56px}
.tr-peek h2{margin:0 0 16px;text-align:center;font-size:15px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.tr-peek-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.tr-peek-item{background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 20px 40px -30px rgba(0,0,0,.6)}
.tr-peek-item img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover}
.tr-peek-item p{margin:0;padding:10px 12px 12px;font-size:14px;font-weight:600;line-height:1.3}
.tr-list{width:100%;max-width:1080px;margin:0 auto;padding:12px 20px 56px;display:flex;flex-direction:column;gap:20px}
.tr-row{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);align-items:center;gap:36px;background:#fff;border-radius:24px;padding:20px;box-shadow:0 30px 60px -40px rgba(0,0,0,.6)}
.tr-row.flip .tr-thumb{order:2}
.tr-thumb{display:block;border-radius:14px;overflow:hidden;transition:transform .2s ease}
.tr-thumb:hover{transform:scale(1.015)}
.tr-thumb img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover}
.tr-text{display:flex;flex-direction:column;align-items:flex-start;gap:12px;padding:4px 8px}
.tr-num{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;letter-spacing:.08em;color:var(--mut)}
.tr-num b{color:var(--k);background:var(--y);border-radius:999px;padding:4px 10px}
.tr-text h2{margin:0;font-size:28px;line-height:1.12;font-weight:700;letter-spacing:-.025em;text-wrap:balance}
.tr-text p{margin:0;font-size:16px;line-height:1.5;color:var(--mut);text-wrap:pretty}
.tr-open{width:auto;margin-top:6px;padding:14px 22px;font-size:15.5px}
.tr-foot{text-align:center;font-size:12.5px;color:rgba(10,10,10,.7);padding:0 20px 24px}
.tr-foot a{color:inherit}
@container tr (max-width:760px){
.tr-bar{font-size:18px;padding:10px 16px;gap:8px}
.tr-bar svg{width:24px;height:24px}
.tr-hero{padding:22px 16px 18px;gap:11px}
.tr-tag{font-size:12.5px;padding:6px 13px}
.tr h1{font-size:min(38px,10cqi);letter-spacing:-.03em}
.tr-sub{font-size:15.5px}
.tr-card{padding:14px;border-radius:16px}
.tr-btn{font-size:15.5px;padding:15px 16px}
.tr-peek{padding:4px 16px 40px}
.tr-peek-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.tr-peek-item p{font-size:12.5px;padding:8px 10px 10px}
.tr-list{padding:8px 16px 40px;gap:14px}
.tr-row{grid-template-columns:1fr;gap:14px;padding:12px;border-radius:18px}
.tr-row.flip .tr-thumb{order:0}
.tr-text{padding:0 4px 6px;gap:10px}
.tr-text h2{font-size:21px}
.tr-text p{font-size:15px}
.tr-open{width:100%}
}
`

const VbMark = () => (
    <svg viewBox="0 0 100 100" fill="none" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="M58 6.5A44 44 0 0 1 42 93.3" stroke="#ED7D37" />
        <path d="M38 93.4A44 44 0 0 1 54 6.2" stroke="#fff" />
        <path d="M25 34l12 30L58 12" stroke="#ED7D37" />
        <path d="M58 12L38 88" stroke="#fff" />
        <path d="M51 36h15a7 7 0 0 1 0 14H48h19a7 7 0 0 1 0 14H44" stroke="#fff" />
    </svg>
)

const YtLogo = () => (
    <svg viewBox="0 0 28 20" aria-hidden="true">
        <rect width="28" height="20" rx="5.5" fill="#FF0000" />
        <path d="M11.2 5.8v8.4l7.2-4.2z" fill="#fff" />
    </svg>
)

const Arrow = () => (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="M5 12h14M13 6l6 6-6 6" />
    </svg>
)

function Pill({ text }: { text: string }) {
    return (
        <span className="tr-tag">
            {text.split(/(YouTube)/).map((p, i) =>
                p === "YouTube" ? (
                    <span className="tr-yt" key={i}>
                        <YtLogo />
                        YouTube
                    </span>
                ) : (
                    <span key={i}>{p}</span>
                )
            )}
        </span>
    )
}

// "Get My 9 Free YouTube Trainings" → the last two words get the yellow highlight.
function Headline({ text }: { text: string }) {
    const words = text.trim().split(/\s+/)
    const cut = Math.max(words.length - 2, 0)
    return (
        <h1>
            {words.slice(0, cut).join(" ")} <em>{words.slice(cut).join(" ")}</em>
        </h1>
    )
}

function OptInView({ headline, sub, pill }: { headline: string; sub: string; pill: string }) {
    const [sending, setSending] = useState(false)
    const [err, setErr] = useState("")

    // Visitors who went through Kit's EU consent step come back with ?sent=1.
    useEffect(() => {
        if (typeof window !== "undefined" && new URLSearchParams(window.location.search).get("sent") === "1") {
            window.location.replace(CONFIRMED)
        }
    }, [])

    async function submit(e: any) {
        e.preventDefault()
        const email = String(new FormData(e.currentTarget).get("email") || "").trim()
        if (!email) return setErr("Please enter your email address.")
        setErr("")
        setSending(true)
        const body = new URLSearchParams()
        body.set("email_address", email)
        body.append("tags[]", String(TAG))
        try {
            const res = await fetch(`https://app.kit.com/forms/${FORM}/subscriptions`, {
                method: "POST",
                headers: { Accept: "application/json" },
                body,
            })
            const data = await res.json().catch(() => ({}))
            if (!res.ok || data.status === "failed") throw new Error(data?.errors?.messages?.[0] || "failed")
            try {
                ;(window as any).fbq?.("track", "Lead", { content_name: "trainings" })
            } catch (_) {}
            if (data?.status === "quarantined" && data?.url) {
                // Kit's bot check: the visitor proves they're human on Kit's page, then Kit finishes the sign-up.
                window.location.href = data.url
                return
            }
            if (data?.consent?.enabled && data?.consent?.url) {
                // EU visitors confirm consent on Kit's page, then come straight back to the library.
                const u = new URL(data.consent.url)
                u.searchParams.set("redirect", window.location.origin + CONFIRMED)
                u.searchParams.delete("response_format")
                window.location.href = u.toString()
                return
            }
            window.location.href = CONFIRMED
        } catch (_) {
            setSending(false)
            setErr("Something went wrong. Please check your email address and try again.")
        }
    }

    return (
        <>
            <section className="tr-hero">
                <span className="tr-blob" style={{ width: 420, height: 420, left: -140, top: -160, background: "#FBD357" }} />
                <span className="tr-blob" style={{ width: 480, height: 480, right: -180, bottom: -220, background: "#F7A36A" }} />
                {pill && <Pill text={pill} />}
                <Headline text={headline} />
                <p className="tr-sub">{sub}</p>
                <div className="tr-card">
                    <form className="tr-form" onSubmit={submit} noValidate>
                        <input name="email" type="email" autoComplete="email" inputMode="email" placeholder="Email Address" aria-label="Email Address" required />
                        <button className="tr-btn" type="submit" disabled={sending}>
                            {sending ? "Sending…" : "Get Instant Access"}
                            {!sending && <Arrow />}
                        </button>
                        {err && <p className="tr-err">{err}</p>}
                        <p className="tr-fine">
                            We'll email you every training. Unsubscribe anytime. <a href="/privacy-policy">Privacy Policy</a>
                        </p>
                    </form>
                </div>
            </section>
            <section className="tr-peek" aria-label="What's inside">
                <h2>What's inside</h2>
                <div className="tr-peek-grid">
                    {TRAININGS.map((t) => (
                        <div className="tr-peek-item" key={t.keyword}>
                            <img src={t.thumb} alt="" loading="lazy" />
                            <p>
                                {t.title} {t.mark}
                            </p>
                        </div>
                    ))}
                </div>
            </section>
        </>
    )
}

function LibraryView({ headline, sub, pill }: { headline: string; sub: string; pill: string }) {
    return (
        <>
            <section className="tr-hero">
                <span className="tr-blob" style={{ width: 420, height: 420, left: -140, top: -160, background: "#FBD357" }} />
                <span className="tr-blob" style={{ width: 480, height: 480, right: -180, bottom: -220, background: "#F7A36A" }} />
                {pill && <Pill text={pill} />}
                <Headline text={headline} />
                <p className="tr-sub">{sub}</p>
            </section>
            <section className="tr-list" aria-label="Trainings">
                {TRAININGS.map((t, i) => (
                    <article className={i % 2 ? "tr-row flip" : "tr-row"} key={t.keyword}>
                        <a className="tr-thumb" href={t.doc} target="_blank" rel="noopener" aria-label={`Open ${t.title} ${t.mark}`}>
                            <img src={t.thumb} alt="" loading={i < 2 ? "eager" : "lazy"} />
                        </a>
                        <div className="tr-text">
                            <span className="tr-num">
                                <b>{t.keyword}</b> TRAINING {i + 1} OF {TRAININGS.length}
                            </span>
                            <h2>
                                {t.title} <em>{t.mark}</em>
                            </h2>
                            <p>{t.sub}</p>
                            <a className="tr-btn tr-open" href={t.doc} target="_blank" rel="noopener">
                                Open the training <Arrow />
                            </a>
                        </div>
                    </article>
                ))}
            </section>
        </>
    )
}

/**
 * @framerSupportedLayoutWidth any
 * @framerSupportedLayoutHeight any-prefer-fixed
 * @framerIntrinsicWidth 1200
 * @framerIntrinsicHeight 1600
 */
export default function Trainings(props: { mode?: "optin" | "library"; pill?: string; headline?: string; sub?: string }) {
    const { mode = "optin", pill = "Free YouTube Trainings" } = props
    const n = TRAININGS.length
    const headline =
        props.headline || (mode === "library" ? `You're In. Here Are All ${n} Trainings` : `Get My ${n} Free YouTube Trainings`)
    const sub =
        props.sub ||
        (mode === "library"
            ? "Every guide is below and on its way to your inbox. Please reply YES to that email so I know you got it."
            : "Every guide we use to get our clients views and sales from YouTube: scripts, thumbnails, editing, ideas and the algorithm. Enter your email and get all of them now.")

    return (
        <div className="tr">
            <style>{CSS}</style>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" />
            <a className="tr-bar" href="/" aria-label="Viral Bangers home">
                <VbMark />
                ViralBangers
            </a>
            <main>
                {mode === "library" ? (
                    <LibraryView headline={headline} sub={sub} pill={pill} />
                ) : (
                    <OptInView headline={headline} sub={sub} pill={pill} />
                )}
            </main>
            <footer className="tr-foot">
                © 2026 Viral Bangers Pte. Ltd. All rights reserved. <a href="/privacy-policy">Privacy Policy</a> |{" "}
                <a href="/terms-and-conditions">Terms & Conditions</a>
            </footer>
        </div>
    )
}

addPropertyControls(Trainings, {
    mode: {
        type: ControlType.Enum,
        title: "Page",
        options: ["optin", "library"],
        optionTitles: ["Opt-in", "Library (thank you)"],
        defaultValue: "optin",
    },
    pill: { type: ControlType.String, title: "Pill", defaultValue: "Free YouTube Trainings" },
    headline: { type: ControlType.String, title: "Headline", defaultValue: "", placeholder: "Auto (uses the training count)" },
    sub: { type: ControlType.String, title: "Subhead", defaultValue: "", displayTextArea: true, placeholder: "Auto" },
})
