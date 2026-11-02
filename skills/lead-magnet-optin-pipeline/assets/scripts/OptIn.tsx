// Lead magnet opt-in page (one per guide: /script, /scott, /thumbnails, /million, /algorithm, /ideas, /setup, /edit, /claude),
// plus the newsletter opt-in (/newsletter), which sends people on to /newsletter-confirmed instead of showing a guide link.
// The form posts straight to the guide's Kit form, which saves name, email, phone and the guide's tag.
// Kit then starts that guide's "LM Delivery" sequence, which emails the link. The page also shows the link right away.
import { useEffect, useState } from "react"
import { addPropertyControls, ControlType } from "framer"

type Magnet = {
    form: number
    tag: number
    doc: string
    h1: string
    mark: string
    sub: string
    button: string
    // Optional: page to send people to after they subscribe (instead of showing the guide link).
    redirect?: string
    fine?: string
}

const DOC = "https://docs.google.com/document/d/"

const MAGNETS: Record<string, Magnet> = {
    script: {
        form: 10010068,
        tag: 24299541,
        doc: DOC + "1OnxBRiIg-9a8PKmah0Ani9zUF0RS0fGpLmVhh5A1xsk/edit",
        h1: "The Script Behind Jordan Welch's",
        mark: "923,571-View Video",
        sub: "A line-by-line breakdown of the script we wrote for Jordan, so you can write scripts that keep people watching to the end.",
        button: "Download Your Free Script Breakdown",
    },
    scott: {
        form: 10010079,
        tag: 24299537,
        doc: DOC + "14JHrz6mIf3rHIYbzqLa_GdaU-cp0jq-zLl1NWMcUI1I/edit",
        h1: "How Scott Taylor Tracks",
        mark: "About $40,000 a Month Back to YouTube",
        sub: "The full case study: how a channel he thought was dead became his best source of clients, and how he traces every call back to a video.",
        button: "Download Your Free Case Study",
    },
    thumbnails: {
        form: 10010080,
        tag: 24299539,
        doc: DOC + "1gz4VoJxQW9mt_qVE0l27R_-AwdxTiEZDQ7w_4YUsf3A/edit",
        h1: "The 6-Part Thumbnail Formula That Gets RP Profits",
        mark: "4.4x the Views",
        sub: "Every part of the formula, shown on the real thumbnails we made for RP Profits, so you can use it on your next video.",
        button: "Download Your Free Thumbnail Formula",
    },
    million: {
        form: 10010081,
        tag: 24299540,
        doc: DOC + "1G6gyDiWEyE6oTNBS56qdIFeZ8Fh6ox_41vsOz2TeuN8/edit",
        h1: "How We Got Inayah McMillan",
        mark: "1,185,797 Views on One Video",
        sub: "The positioning behind her first video with us, and how to find the angle only you can make.",
        button: "Download Your Free Case Study",
    },
    algorithm: {
        form: 10010082,
        tag: 24332416,
        doc: DOC + "1uKia2GXBI592Nrk6-4wS_m_49b0uG7ifWi3uqPEW5R8/edit",
        h1: "The New Rules of",
        mark: "The YouTube Algorithm (for 2027)",
        sub: "How YouTube decides which videos to push now, and what to change on your next upload so it gets pushed instead of buried.",
        button: "Download Your Free Algorithm Guide",
    },
    ideas: {
        form: 10010083,
        tag: 24332417,
        doc: DOC + "1zzV1Vz8aGbl24ftDvYGTMoSuV8sTb4INJ5hE9U-Lak8/edit",
        h1: "How To Come Up With BANGER Video Ideas",
        mark: "That Build Your Brand And Get You Sales",
        sub: "The way we pick topics and formats for our clients, so your videos bring in sales, not just views.",
        button: "Download Your Free Video Ideas Guide",
    },
    setup: {
        form: 10010084,
        tag: 24332418,
        doc: DOC + "1-gyDLFbtP6LnwG2-gsfRMVzYnaAg5UWPiS-0txBdTfU/edit",
        h1: "The Only Setup Guide You Need",
        mark: "For Recording YouTube Videos",
        sub: "The camera, mic and lighting to buy at three budgets, so you can film at home and look the part.",
        button: "Download Your Free Setup Guide",
    },
    edit: {
        form: 10010085,
        tag: 24299538,
        doc: DOC + "1-qo8fvNmqzGHifdI28FOddSi3QM-QtveNpd82FLQ-BQ/edit",
        h1: "The Editing Checklist Behind 100M Views",
        mark: "For Business YouTube Channels",
        sub: "The checklist we use when we edit Chamath Palihapitiya's channel, so every video is easier to watch to the end.",
        button: "Download Your Free Editing Checklist",
    },
    claude: {
        form: 10010086,
        tag: 24333917,
        doc: DOC + "1VxLy8Jy2nu7GVoJXXI3lvYyA62j5LmixJq82Dq6FwyA/edit",
        h1: "How To Edit YouTube Videos",
        mark: "Using Claude",
        sub: "My full guide to editing with Claude, with every prompt I use, so you can edit faster with AI.",
        button: "Download Your Free Claude Guide",
    },
}

MAGNETS.newsletter = {
    form: 10020943,
    tag: 24419564,
    doc: "",
    h1: "The Daily Email That Shows You How To Get Clients From",
    mark: "YouTube Without Ads",
    sub: "One email a day: real client case studies, the video formats we use, and what's working on YouTube right now. Free.",
    button: "Subscribe To The Newsletter",
    redirect: "/newsletter-confirmed",
    fine: "One email a day. Unsubscribe anytime.",
}

const KEYS = Object.keys(MAGNETS)

const CSS = `
.oi{--o:#ED7D37;--y:#FBD357;--c:#FFF2E8;--k:#0A0A0A;--mut:#5E554E;--line:rgba(10,10,10,.12);
font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--k);background:var(--o);width:100%;min-height:100vh;-webkit-font-smoothing:antialiased;container-type:inline-size;container-name:oi;display:flex;flex-direction:column}
.oi *{box-sizing:border-box}
.oi-bar{display:flex;justify-content:center;align-items:center;gap:10px;background:var(--k);color:#fff;padding:13px 16px;font-size:22px;font-weight:700;letter-spacing:-.02em;line-height:1}
.oi-bar svg{width:30px;height:30px;flex:none}
.oi-main{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding:28px 20px 56px;gap:14px;position:relative;overflow:hidden}
.oi-blob{position:absolute;border-radius:50%;filter:blur(70px);opacity:.45;pointer-events:none}
.oi-main>*:not(.oi-blob){position:relative}
.oi-rate{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600}
.oi-rate b{color:var(--k);letter-spacing:1px}
.oi-tag{display:inline-flex;align-items:center;background:var(--k);color:#fff;border-radius:999px;padding:9px 18px;font-size:15px;font-weight:600;box-shadow:0 2px 0 rgba(10,10,10,.18)}
.oi-yt{display:inline-flex;align-items:center;gap:.3em;margin:0 .3em}
.oi-yt svg{width:1.35em;height:auto}
.oi h1{margin:6px 0 0;font-size:54px;line-height:1.02;font-weight:700;letter-spacing:-.035em;max-width:900px;text-wrap:balance}
.oi h1 em{font-style:normal;background:linear-gradient(transparent 58%,var(--y) 58%,var(--y) 94%,transparent 94%);-webkit-box-decoration-break:clone;box-decoration-break:clone}
.oi-sub{margin:0;font-size:19px;line-height:1.45;font-weight:500;max-width:640px;text-wrap:pretty}
.oi-card{width:100%;max-width:520px;margin-top:10px;background:#fff;border-radius:20px;padding:20px;box-shadow:0 30px 60px -36px rgba(0,0,0,.55);text-align:left}
.oi-form{display:flex;flex-direction:column;gap:10px}
.oi-form input{width:100%;font:inherit;font-size:16px;padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:var(--c);color:var(--k);outline:none}
.oi-form input:focus{border-color:var(--k);background:#fff}
.oi-btn{appearance:none;border:0;cursor:pointer;width:100%;font:inherit;font-size:17px;font-weight:700;letter-spacing:-.01em;color:#fff;background:var(--k);border-radius:999px;padding:17px 20px;margin-top:4px;display:inline-flex;justify-content:center;align-items:center;gap:10px;text-decoration:none;transition:transform .2s ease,box-shadow .2s ease;box-shadow:0 10px 24px -14px rgba(0,0,0,.6)}
.oi-btn:hover{transform:translateY(-1px)}
.oi-btn:disabled{opacity:.6;cursor:wait}
.oi-btn svg{width:18px;height:18px}
.oi-fine{margin:10px 0 0;font-size:12.5px;color:var(--mut);text-align:center;line-height:1.4}
.oi-fine a{color:inherit}
.oi-err{margin:4px 0 0;font-size:14px;color:#B3261E;font-weight:600;text-align:center}
.oi-done{display:flex;flex-direction:column;gap:10px;text-align:center}
.oi-done h2{margin:0;font-size:26px;letter-spacing:-.02em}
.oi-done p{margin:0;font-size:16px;line-height:1.45}
.oi-check{width:52px;height:52px;border-radius:50%;background:#54FA80;display:grid;place-items:center;margin:0 auto 4px;font-size:26px}
.oi-foot{text-align:center;font-size:12.5px;color:rgba(10,10,10,.7);padding:0 20px 24px}
.oi-foot a{color:inherit}
@container oi (max-width:760px){
.oi-bar{font-size:18px;padding:10px 16px;gap:8px}
.oi-bar svg{width:24px;height:24px}
.oi-main{padding:20px 16px 44px;gap:11px}
.oi-rate{font-size:12.5px}
.oi-tag{font-size:12.5px;padding:6px 13px}
.oi h1{font-size:min(36px,9.4cqi);letter-spacing:-.03em}
.oi-sub{font-size:15.5px}
.oi-card{padding:14px;border-radius:16px}
.oi-form input{padding:13px 14px}
.oi-btn{font-size:15.5px;padding:15px 16px}
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

/**
 * @framerSupportedLayoutWidth any
 * @framerSupportedLayoutHeight any-prefer-fixed
 * @framerIntrinsicWidth 1200
 * @framerIntrinsicHeight 900
 */
export default function OptIn(props: { magnet?: string; rating?: string; icp?: string }) {
    const { magnet = "script", rating = "Trusted by 100+ coaches", icp = "For Coaches Already Doing YouTube" } = props
    const m = MAGNETS[magnet] || MAGNETS.script
    const [state, setState] = useState<"idle" | "sending" | "done">("idle")
    const [err, setErr] = useState("")

    // Visitors who went through Kit's EU consent step come back with ?sent=1.
    useEffect(() => {
        if (typeof window !== "undefined" && new URLSearchParams(window.location.search).get("sent") === "1") {
            if (m.redirect) window.location.replace(m.redirect)
            else setState("done")
        }
    }, [])

    async function submit(e: any) {
        e.preventDefault()
        const f = new FormData(e.currentTarget)
        const name = String(f.get("name") || "").trim()
        const email = String(f.get("email") || "").trim()
        const phone = String(f.get("phone") || "").trim()
        if (!name || !email || !phone) return setErr("Please fill in all three fields.")
        setErr("")
        setState("sending")
        const parts = name.split(/\s+/)
        const body = new URLSearchParams()
        body.set("email_address", email)
        body.set("first_name", parts[0])
        if (parts.length > 1) body.set("last_name", parts.slice(1).join(" "))
        body.set("fields[phone_number]", phone)
        body.append("tags[]", String(m.tag))
        try {
            const res = await fetch(`https://app.kit.com/forms/${m.form}/subscriptions`, {
                method: "POST",
                headers: { Accept: "application/json" },
                body,
            })
            const data = await res.json().catch(() => ({}))
            if (!res.ok || data.status === "failed") throw new Error(data?.errors?.messages?.[0] || "failed")
            try {
                ;(window as any).fbq?.("track", "Lead", { content_name: magnet })
            } catch (_) {}
            if (data?.status === "quarantined" && data?.url) {
                // Kit's bot check: the visitor proves they're human on Kit's page, then Kit finishes the sign-up.
                window.location.href = data.url
                return
            }
            if (data?.consent?.enabled && data?.consent?.url) {
                // EU visitors confirm consent on Kit's page, then come straight back here.
                const back = window.location.origin + (m.redirect || window.location.pathname + "?sent=1")
                const u = new URL(data.consent.url)
                u.searchParams.set("redirect", back)
                u.searchParams.delete("response_format")
                window.location.href = u.toString()
                return
            }
            if (m.redirect) {
                window.location.href = m.redirect
                return
            }
            setState("done")
        } catch (_) {
            setState("idle")
            setErr("Something went wrong. Please check your email address and try again.")
        }
    }

    const icpParts = icp.split(/(YouTube)/)
    return (
        <div className="oi">
            <style>{CSS}</style>
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" />
            <header className="oi-bar" role="banner">
                <VbMark />
                ViralBangers
            </header>
            <main className="oi-main">
                <span className="oi-blob" style={{ width: 420, height: 420, left: -140, top: -160, background: "#FBD357" }} />
                <span className="oi-blob" style={{ width: 480, height: 480, right: -180, bottom: -200, background: "#F7A36A" }} />
                {rating && (
                <span className="oi-rate">
                    <b>★★★★★</b> {rating}
                </span>
                )}
                {icp && (
                <span className="oi-tag">
                    <span style={{ marginRight: ".3em" }}>⭐</span>
                    {icpParts.map((p, i) =>
                        p === "YouTube" ? (
                            <span className="oi-yt" key={i}>
                                <YtLogo />
                                YouTube
                            </span>
                        ) : (
                            <span key={i}>{p}</span>
                        )
                    )}
                    <span style={{ marginLeft: ".3em" }}>⭐</span>
                </span>
                )}
                <h1>
                    {m.h1} <em>{m.mark}</em>
                </h1>
                <p className="oi-sub">{m.sub}</p>
                <div className="oi-card">
                    {state === "done" ? (
                        <div className="oi-done" role="status">
                            <div className="oi-check" aria-hidden="true">✓</div>
                            <h2>It's on its way to your inbox</h2>
                            <p>Check your email for the guide. Please reply YES to it so I know you got it.</p>
                            <a className="oi-btn" href={m.doc} target="_blank" rel="noopener">
                                Open the guide now <Arrow />
                            </a>
                        </div>
                    ) : (
                        <form className="oi-form" onSubmit={submit} noValidate>
                            <input name="name" type="text" autoComplete="name" placeholder="Full Name" aria-label="Full Name" required />
                            <input name="email" type="email" autoComplete="email" inputMode="email" placeholder="Email Address" aria-label="Email Address" required />
                            <input name="phone" type="tel" autoComplete="tel" inputMode="tel" placeholder="Phone Number" aria-label="Phone Number" required />
                            <button className="oi-btn" type="submit" disabled={state === "sending"}>
                                {state === "sending" ? "Sending…" : m.button}
                                {state !== "sending" && <Arrow />}
                            </button>
                            {err && <p className="oi-err">{err}</p>}
                            <p className="oi-fine">
                                {m.fine || "We'll email you the guide. Unsubscribe anytime."} <a href="/privacy-policy">Privacy Policy</a>
                            </p>
                        </form>
                    )}
                </div>
            </main>
            <footer className="oi-foot">
                © 2026 Viral Bangers Pte. Ltd. All rights reserved. <a href="/privacy-policy">Privacy Policy</a> |{" "}
                <a href="/terms-and-conditions">Terms & Conditions</a>
            </footer>
        </div>
    )
}

addPropertyControls(OptIn, {
    magnet: {
        type: ControlType.Enum,
        title: "Guide",
        options: KEYS,
        optionTitles: KEYS.map((k) => k.toUpperCase()),
        defaultValue: "script",
    },
    rating: { type: ControlType.String, title: "Rating line", defaultValue: "Trusted by 100+ coaches" },
    icp: { type: ControlType.String, title: "Who it's for", defaultValue: "For Coaches Already Doing YouTube" },
})
