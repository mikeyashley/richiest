#!/usr/bin/env python3
"""
Retouch all ETF pages to match BIL template structure.
Inserts new sections (bottom line, overview, pros/cons, personas, scenarios, comparison, verdict)
after the author box, before the first existing content section.
"""

import os
import re

BASE = "/Users/michael/Documents/GitHub/richiest/etfs"

# ETF metadata: ticker -> (display_name, category, eyebrow, description, pros, cons, personas, scenarios, comp1, comp2, verdict)
ETF_DATA = {
    # Bond
    "agg": {
        "name": "AGG — iShares Core U.S. Aggregate Bond ETF",
        "eyebrow": "Bond ETFs",
        "category": "bond",
        "asset_class": "Fixed Income Bond ETF",
        "strategy": "Total Bond Market",
        "frequency": "Monthly",
        "expense": "0.03%",
        "sponsor_name": "iShares (BlackRock)",
        "sponsor_url": "https://www.ishares.com/us/products/239458/ishares-core-total-us-bond-market-etf",
        "quick_take": "AGG is the go-to bond fund for diversification and portfolio stability. It's ideal for moderate investors seeking income with less volatility than stocks.",
        "bluf": "The <strong>iShares Core U.S. Aggregate Bond ETF (AGG)</strong> is a broad, low-cost bond fund that holds thousands of U.S. investment-grade bonds — Treasuries, corporate bonds, and mortgage-backed securities all in one package. Think of it as the S&P 500 for bonds: a single fund that gives you a wide, diversified slice of the entire investment-grade U.S. bond market. It pays monthly income and is widely used to balance stock-heavy portfolios.",
        "overview_title": "AGG Explained: What It Is and Why It Matters",
        "overview_body": """<p>When people talk about "adding bonds to your portfolio," they often mean a fund like <strong>AGG</strong>. It's the largest and most popular bond ETF in the world, holding over 10,000 bonds spanning U.S. Treasuries, corporate debt, and government-backed mortgage securities.</p>
        <p>Here's why investors reach for AGG:</p>
        <ul>
            <li><strong>Instant Diversification:</strong> One fund covers virtually the entire U.S. investment-grade bond universe.</li>
            <li><strong>Monthly Income:</strong> AGG pays dividends every month from the interest earned on its bonds.</li>
            <li><strong>Portfolio Ballast:</strong> Bonds often move opposite to stocks. When markets fall, AGG tends to hold steady or rise — a classic buffer.</li>
        </ul>
        <p>Managed by <strong>BlackRock's iShares</strong>, the world's largest ETF provider, AGG tracks the Bloomberg U.S. Aggregate Bond Index.</p>""",
        "facts": [("AGG", "Fixed Income Bond ETF", "Total Bond Market", "Monthly", "0.03%", "iShares (BlackRock)", "https://www.ishares.com/us/products/239458/ishares-core-total-us-bond-market-etf")],
        "pros": [
            ("Extremely Broad Diversification", "Thousands of bonds in one fund — instant exposure to the entire U.S. investment-grade bond market."),
            ("Lowest Possible Cost", "At 0.03%, nearly free to own. Cost drag is minimal over decades."),
            ("Monthly Income", "Regular monthly dividend payments from bond interest — predictable cash flow."),
            ("Portfolio Stabilizer", "Historically reduces portfolio volatility when paired with stock funds."),
        ],
        "cons": [
            ("Interest Rate Risk", "When rates rise, bond prices fall. AGG can lose value in rising-rate environments."),
            ("Low Yield in Low-Rate Environments", "When rates are low, AGG's income is modest — may not beat inflation."),
            ("No Inflation Protection", "Standard bonds lose purchasing power if inflation runs hot for long periods."),
            ("Not a Growth Investment", "AGG won't compound wealth like stocks over the long run. It's a stabilizer, not an accelerator."),
        ],
        "personas": [
            ("fa-balance-scale", "The '60/40 Builder'", "You've built a solid stock portfolio and now want to reduce volatility by adding bonds. AGG is the classic complement — simple, cheap, and effective."),
            ("fa-umbrella", "The Near-Retiree", "You're 5–10 years from retirement and want to preserve what you've built. Shifting some money into AGG provides income and cushion against market downturns."),
            ("fa-coins", "The Income Seeker", "You want reliable monthly income without the risk of individual bonds. AGG delivers just that — a steady stream of interest payments backed by thousands of bonds."),
        ],
        "scenarios": [
            ("Rebalancing Into Safety", "You've had a strong stock year and want to lock in some gains. You shift 20% of your portfolio into AGG to reduce risk heading into uncertainty, while still earning monthly income."),
            ("Offsetting Stock Volatility", "During a market correction, your stocks drop 15% but your AGG holding barely moves — cushioning the overall portfolio blow and keeping your nerves steady."),
        ],
        "comp1_ticker": "BND",
        "comp1_name": "Vanguard Total Bond Market ETF",
        "comp1_hold": "U.S. investment-grade bonds",
        "comp1_why": "Nearly identical to AGG but from Vanguard — same strategy, same cost, personal preference decides.",
        "comp2_ticker": "SCHZ",
        "comp2_name": "Schwab U.S. Aggregate Bond ETF",
        "comp2_hold": "U.S. investment-grade bonds",
        "comp2_why": "Schwab's version of the same index — another near-clone at ultra-low cost.",
        "verdict": "AGG is the simplest, most cost-effective way to add broad bond exposure to your portfolio. It won't make you rich, but it will keep you sane during stock market storms. If you're building a balanced long-term portfolio, <strong>AGG belongs in it.</strong>",
        "verdict_cta": "If stability, income, and diversification matter to you — <strong>AGG is the standard bearer. Add it and sleep better.</strong>",
    },

    # Index ETFs
    "voo": {
        "name": "VOO — Vanguard S&P 500 ETF",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / S&P 500 Index",
        "frequency": "Quarterly",
        "expense": "0.03%",
        "sponsor_name": "Vanguard",
        "sponsor_url": "https://investor.vanguard.com/etf/profile/VOO",
        "quick_take": "VOO is the gold-standard S&P 500 ETF — ultra-cheap, tax-efficient, and the core holding for millions of long-term investors.",
        "bluf": "The <strong>Vanguard S&P 500 ETF (VOO)</strong> is about as simple and powerful as investing gets. It owns a slice of every company in the S&P 500 — the 500 largest U.S. businesses — at a cost so low it's practically free. No manager trying to beat the market, no guessing which stock to buy. Just steady, automatic exposure to American corporate greatness. For most normal investors, VOO *is* the portfolio.",
        "overview_title": "VOO Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>VOO</strong> tracks the S&P 500 Index — the benchmark that includes Apple, Microsoft, Amazon, NVIDIA, and 496 other leading American companies. When the U.S. economy does well, VOO does well. It's as close to "owning America" as you can get in one ticker.</p>
        <p>Why investors love VOO:</p>
        <ul>
            <li><strong>Near-Zero Cost:</strong> At 0.03%, you keep almost every dollar of return the market produces.</li>
            <li><strong>Broad Diversification:</strong> 500 companies across all major sectors — no single stock can sink you.</li>
            <li><strong>Long-Term Track Record:</strong> The S&P 500 has historically returned ~10% annually over the long run.</li>
            <li><strong>Tax Efficiency:</strong> Vanguard's unique structure minimizes capital gains distributions.</li>
        </ul>
        <p>Managed by <strong>Vanguard</strong>, the pioneer of low-cost investing, VOO is one of the largest ETFs on Earth with over $1 trillion in assets.</p>""",
        "pros": [
            ("Lowest Cost in Class", "0.03% expense ratio — essentially free. Over 30 years, this saves thousands vs. higher-cost alternatives."),
            ("Instant 500-Stock Diversification", "One purchase gives you exposure to the entire S&P 500 — the most tracked benchmark in investing."),
            ("Proven Long-Term Performance", "The S&P 500 has rewarded patient investors with ~10% average annual returns historically."),
            ("Tax Efficiency", "Vanguard's patent-protected structure virtually eliminates taxable capital gains distributions."),
        ],
        "cons": [
            ("U.S. Only Exposure", "No international diversification — missing out on growth in Europe, Asia, and emerging markets."),
            ("Market Risk", "VOO follows the market up and down. In a recession, it can drop 30–50%."),
            ("Quarterly Dividends Only", "Dividend yield is modest (~1.3–1.5%) — not for income-focused investors."),
            ("No Small Cap Exposure", "Only large-cap stocks — misses potential from smaller, faster-growing companies."),
        ],
        "personas": [
            ("fa-seedling", "The Long-Term Wealth Builder", "You're in your 20s–40s and just want to grow wealth over decades without thinking about it. VOO is your answer — buy regularly, hold forever."),
            ("fa-home", "The Practical 'Set It & Forget It' Investor", "You don't want to research stocks. You want one ETF that does the work. VOO has your back — it IS the market."),
            ("fa-chart-line", "The Core Portfolio Builder", "You're constructing a diversified portfolio and need a reliable foundation. VOO as 60–80% of your equity allocation is textbook smart investing."),
        ],
        "scenarios": [
            ("Dollar-Cost Averaging Into Retirement", "You invest $500/month into VOO no matter what the market does. Over 30 years at historical returns, that modest monthly commitment grows to over $1 million."),
            ("Riding Out a Market Crash", "VOO drops 35% in a bear market. Instead of panicking, you keep buying — because history shows the S&P 500 has always recovered and gone on to new highs."),
        ],
        "comp1_ticker": "SPY",
        "comp1_name": "SPDR S&P 500 ETF Trust",
        "comp1_hold": "S&P 500 Index",
        "comp1_why": "The original S&P 500 ETF — more liquid, preferred by traders. VOO is better for long-term buy-and-hold due to lower cost.",
        "comp2_ticker": "IVV",
        "comp2_name": "iShares Core S&P 500 ETF",
        "comp2_hold": "S&P 500 Index",
        "comp2_why": "BlackRock's version — matches VOO's 0.03% cost. Nearly identical; comes down to preference of custodian.",
        "verdict": "VOO is the single best investment for the average long-term investor. It's what Warren Buffett recommends for most people's portfolios. Cheap, diversified, and historically powerful. <strong>If you own nothing else, own VOO.</strong>",
        "verdict_cta": "Stop overthinking it. <strong>Buy VOO, hold it forever, and let compounding do its magic.</strong>",
    },

    "spy": {
        "name": "SPY — SPDR S&P 500 ETF Trust",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / S&P 500 Index",
        "frequency": "Quarterly",
        "expense": "0.09%",
        "sponsor_name": "State Street (SSGA)",
        "sponsor_url": "https://www.ssga.com/us/en/individual/etfs/funds/spdr-sp-500-etf-trust-spy",
        "quick_take": "SPY is the world's most traded ETF — the gold standard for active traders and institutional investors seeking S&P 500 exposure.",
        "bluf": "The <strong>SPDR S&P 500 ETF Trust (SPY)</strong> was the first U.S.-listed ETF ever created (1993) and remains the most actively traded. It tracks the same S&P 500 as VOO and IVV, but its massive liquidity makes it the preferred choice for traders, options players, and institutions. For long-term buy-and-hold investors, VOO's lower cost wins — but SPY is the market's heartbeat.",
        "overview_title": "SPY Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>SPY</strong> is the original ETF — launched in 1993, it pioneered the concept of buying and selling the entire stock market like a single share. Today it trades over $20 billion worth of shares daily, making it the most liquid ETF on Earth.</p>
        <p>Why investors use SPY:</p>
        <ul>
            <li><strong>Maximum Liquidity:</strong> Penny-wide bid-ask spreads — in and out instantly at minimal cost.</li>
            <li><strong>Options Market:</strong> The deepest, most liquid options market of any ETF — critical for hedging strategies.</li>
            <li><strong>Institutional Standard:</strong> Used by hedge funds, pension funds, and banks as the benchmark instrument.</li>
            <li><strong>30+ Year Track Record:</strong> The longest history of any S&P 500 ETF.</li>
        </ul>
        <p>Managed by <strong>State Street Global Advisors (SSGA)</strong>, SPY is structured as a Unit Investment Trust — slightly different legal structure from newer ETFs like VOO.</p>""",
        "pros": [
            ("World's Most Liquid ETF", "Trades billions daily — you can move massive positions without affecting the price."),
            ("Deep Options Market", "SPY options are the most actively traded in the world — essential for hedging and income strategies."),
            ("Pioneer ETF with 30+ Year History", "The original — launched 1993, battle-tested through every market cycle."),
            ("Tracks the S&P 500", "Same 500-company exposure as VOO/IVV — broad U.S. large-cap diversification."),
        ],
        "cons": [
            ("Higher Expense Ratio", "At 0.09%, SPY costs 3x more than VOO (0.03%). Over decades, this difference compounds significantly."),
            ("Unit Investment Trust Structure", "Older legal structure means dividends can't be reinvested during the quarter — a minor drag vs. newer ETFs."),
            ("Not Ideal for Buy-and-Hold", "The cost disadvantage makes VOO or IVV better for long-term passive investors."),
            ("Market Risk", "Follows the S&P 500 — in a major crash, SPY falls with it."),
        ],
        "personas": [
            ("fa-bolt", "The Active Trader", "You need to move in and out of S&P 500 positions quickly. SPY's liquidity and tight spreads make it the standard trading vehicle."),
            ("fa-shield-alt", "The Options Strategist", "You use covered calls, protective puts, or spreads to manage risk or generate income. SPY's options market is unmatched in depth."),
            ("fa-university", "The Institutional Investor", "Managing large sums and need to execute S&P 500 exposure without market impact. SPY handles it."),
        ],
        "scenarios": [
            ("Hedging a Stock Portfolio", "You're worried about a short-term market decline but don't want to sell your stocks. You buy SPY put options as insurance — cheap, liquid, and effective."),
            ("Generating Income with Covered Calls", "You hold SPY and sell monthly call options against it — collecting premium income on top of the quarterly dividend."),
        ],
        "comp1_ticker": "VOO",
        "comp1_name": "Vanguard S&P 500 ETF",
        "comp1_hold": "S&P 500 Index",
        "comp1_why": "Lower cost (0.03%) makes VOO better for long-term passive holding. SPY wins on trading/options.",
        "comp2_ticker": "IVV",
        "comp2_name": "iShares Core S&P 500 ETF",
        "comp2_hold": "S&P 500 Index",
        "comp2_why": "BlackRock's version at 0.03% — matches VOO cost, often preferred by Fidelity and Schwab customers.",
        "verdict": "SPY is not the cheapest S&P 500 ETF, but it's the most important. For traders, options users, and institutions, it's irreplaceable. For long-term passive investors, <strong>VOO is the better choice</strong> — but understanding SPY is understanding modern markets.",
        "verdict_cta": "<strong>Trade with SPY. Hold with VOO.</strong> That's the smart investor's playbook.",
    },

    "qqq": {
        "name": "QQQ — Invesco QQQ Trust",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / Nasdaq-100 Index",
        "frequency": "Quarterly",
        "expense": "0.20%",
        "sponsor_name": "Invesco",
        "sponsor_url": "https://www.invesco.com/qqq-etf/",
        "quick_take": "QQQ is the premier tech-growth ETF — tracking the Nasdaq-100's top 100 non-financial companies with a heavy tilt toward mega-cap technology.",
        "bluf": "The <strong>Invesco QQQ Trust (QQQ)</strong> tracks the Nasdaq-100, which holds the 100 largest non-financial companies listed on the Nasdaq exchange. In practice, that means a concentrated bet on technology: Apple, Microsoft, NVIDIA, Alphabet, Meta, Amazon. QQQ has been a rocket ship in bull markets and a gut-punch in corrections. It's for investors who believe tech leads the economy and can stomach volatility.",
        "overview_title": "QQQ Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>QQQ</strong> is often called the "tech ETF," though it includes other sectors too (consumer discretionary, healthcare). Its top 10 holdings routinely account for over 50% of the fund — extremely concentrated compared to the S&P 500.</p>
        <p>Why investors own QQQ:</p>
        <ul>
            <li><strong>Tech Dominance:</strong> Direct exposure to the companies driving AI, cloud, semiconductors, and digital advertising.</li>
            <li><strong>Superior Long-Term Returns:</strong> QQQ has historically outperformed the S&P 500 over most 10+ year periods.</li>
            <li><strong>High Liquidity:</strong> Second only to SPY in daily trading volume.</li>
            <li><strong>Innovation Benchmark:</strong> If you believe innovation drives the next decade, QQQ captures it.</li>
        </ul>
        <p>Managed by <strong>Invesco</strong>, QQQ has over $250 billion in assets and has been around since 1999.</p>""",
        "pros": [
            ("Exceptional Long-Term Growth", "QQQ has vastly outperformed the S&P 500 over the past 10–20 years, driven by mega-cap tech."),
            ("Exposure to Innovation Leaders", "Apple, Microsoft, NVIDIA, Alphabet, Meta — the companies redefining every industry."),
            ("High Liquidity", "Among the most actively traded ETFs — tight spreads, easy execution."),
            ("AI & Tech Tailwind", "Positioned at the epicenter of the artificial intelligence revolution."),
        ],
        "cons": [
            ("Concentrated Risk", "Top 10 holdings = 50%+ of the fund. A bad day for big tech is a bad day for QQQ."),
            ("Higher Volatility", "QQQ swings harder than the S&P 500 — drops of 30–50% in corrections (2000, 2008, 2022)."),
            ("Higher Expense Ratio", "At 0.20%, costlier than VOO (0.03%) or IVV. The gap compounds over decades."),
            ("Low Dividend Yield", "Tech companies reinvest profits — QQQ's yield is minimal (~0.6%). Not for income seekers."),
        ],
        "personas": [
            ("fa-rocket", "The Growth Investor", "You believe technology and innovation will drive superior returns over the next decade and can handle the volatility that comes with it."),
            ("fa-brain", "The AI Believer", "You want concentrated exposure to the companies building artificial intelligence — NVIDIA, Microsoft, Alphabet, Meta. QQQ is your vehicle."),
            ("fa-chart-bar", "The Core + Satellite Investor", "You hold VOO as your core and add QQQ as a growth satellite — boosting tech exposure without going all-in."),
        ],
        "scenarios": [
            ("Riding the AI Wave", "NVIDIA's data center business explodes. QQQ's large NVDA weighting means your investment surges far more than a plain S&P 500 fund would."),
            ("Surviving a Tech Correction", "QQQ drops 35% in a rate-hike cycle. You hold steady (or buy more) knowing that every major tech correction in history has been followed by new highs."),
        ],
        "comp1_ticker": "QQQM",
        "comp1_name": "Invesco Nasdaq-100 ETF",
        "comp1_hold": "Nasdaq-100 Index",
        "comp1_why": "Identical holdings to QQQ but 0.15% expense ratio vs 0.20% — better for long-term buy-and-hold investors.",
        "comp2_ticker": "VGT",
        "comp2_name": "Vanguard Information Technology ETF",
        "comp2_hold": "U.S. tech sector stocks",
        "comp2_why": "Pure tech-sector play at lower cost. More concentrated in tech but excludes Amazon, Alphabet categorized elsewhere.",
        "verdict": "QQQ is the ultimate growth ETF for investors who believe in technology's continued dominance. The volatility is real and the concentration risk is real — but so are the returns. <strong>Use it as a growth booster alongside VOO, not as a replacement.</strong>",
        "verdict_cta": "<strong>Want to own the future? QQQ + VOO is a powerful long-term combination.</strong>",
    },

    "qqqm": {
        "name": "QQQM — Invesco Nasdaq-100 ETF",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / Nasdaq-100 Index",
        "frequency": "Quarterly",
        "expense": "0.15%",
        "sponsor_name": "Invesco",
        "sponsor_url": "https://www.invesco.com/us/financial-products/etfs/product-detail?audienceType=Investor&ticker=QQQM",
        "quick_take": "QQQM is the buy-and-hold investor's version of QQQ — same Nasdaq-100 exposure at a lower cost, designed for retail long-term investors.",
        "bluf": "The <strong>Invesco Nasdaq-100 ETF (QQQM)</strong> is the little sibling of QQQ — same exact portfolio (the Nasdaq-100's top 100 non-financial stocks), but priced at 0.15% instead of 0.20%. Invesco created QQQM specifically for long-term retail investors who don't need QQQ's extreme liquidity for trading. If you're buying and holding, QQQM saves you money every year.",
        "overview_title": "QQQM Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>QQQM</strong> and QQQ hold identical portfolios — the 100 largest non-financial Nasdaq stocks. The difference is cost and audience. QQQ was designed for institutions and traders needing ultra-high liquidity. QQQM was built for regular investors who just want to own the Nasdaq-100 cheaply for the long haul.</p>
        <p>Why choose QQQM over QQQ:</p>
        <ul>
            <li><strong>Lower Cost:</strong> 0.15% vs 0.20% — saves you money over time without giving anything up in return exposure.</li>
            <li><strong>Same Holdings:</strong> Identical to QQQ — Apple, Microsoft, NVIDIA, Alphabet, Meta, Amazon.</li>
            <li><strong>Built for Buy-and-Hold:</strong> Invesco explicitly designed QQQM for retail, long-term investors.</li>
        </ul>
        <p>If you're a trader moving in and out daily, use QQQ. If you're buying and holding for years, use <strong>QQQM</strong>.</p>""",
        "pros": [
            ("Same Nasdaq-100 Power, Lower Cost", "Identical to QQQ at 0.05% cheaper — straightforward win for buy-and-hold investors."),
            ("Tech & Innovation Leaders", "Full exposure to Apple, Microsoft, NVIDIA, Alphabet, Meta, Amazon, and more."),
            ("Long-Term Growth Machine", "Nasdaq-100 has compounded at extraordinary rates over the past 15+ years."),
            ("Retail-Investor Friendly", "Lower share price than QQQ makes it easier to build a position with smaller amounts."),
        ],
        "cons": [
            ("Lower Liquidity Than QQQ", "Less daily trading volume — fine for long-term holders, not ideal for active traders."),
            ("Concentrated Tech Risk", "Top 10 holdings dominate the fund — volatility is higher than the S&P 500."),
            ("No Dividend Income", "Minimal yield (~0.6%) — this is a pure growth vehicle."),
            ("Expense Ratio Still Higher Than VOO", "0.15% vs VOO's 0.03% — relevant if you're primarily seeking broad market exposure."),
        ],
        "personas": [
            ("fa-piggy-bank", "The Long-Term Growth Saver", "You contribute monthly to a growth-focused portfolio and want Nasdaq-100 exposure without overpaying. QQQM is the smart choice over QQQ."),
            ("fa-graduation-cap", "The College Fund Builder", "You're investing for a child's education 10–15 years out. QQQM's tech growth potential can meaningfully outpace broad index funds."),
            ("fa-chart-line", "The QQQ Upgrader", "You already own QQQ and are learning you can get identical exposure at lower cost. Switch to QQQM and keep the compounding gains."),
        ],
        "scenarios": [
            ("Monthly DCA Into Tech Growth", "You invest $300/month into QQQM for 20 years. The lower expense ratio vs QQQ saves you hundreds in fees — and that difference compounds into thousands more at retirement."),
            ("Holding Through Volatility", "Tech sells off 30%. You hold QQQM because you know history — the Nasdaq-100 has recovered from every major drawdown and reached new highs."),
        ],
        "comp1_ticker": "QQQ",
        "comp1_name": "Invesco QQQ Trust",
        "comp1_hold": "Nasdaq-100 Index",
        "comp1_why": "Identical holdings but 0.20% cost. QQQ wins on liquidity for traders; QQQM wins on cost for holders.",
        "comp2_ticker": "ONEQ",
        "comp2_name": "Fidelity Nasdaq Composite ETF",
        "comp2_hold": "Entire Nasdaq Composite (3,000+ stocks)",
        "comp2_why": "Broader than QQQM — includes all Nasdaq stocks, not just the top 100. More diversified but less tech-concentrated.",
        "verdict": "For buy-and-hold investors wanting Nasdaq-100 exposure, QQQM is simply better than QQQ — same thing, lower cost. <strong>No reason to pay more for QQQ if you're not an active trader.</strong>",
        "verdict_cta": "<strong>Switch to QQQM, pocket the savings, and let your tech growth compound unimpeded.</strong>",
    },

    "qqqn": {
        "name": "QQQN — VictoryShares Nasdaq Next 50 ETF",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / Nasdaq Next Generation 100",
        "frequency": "Quarterly",
        "expense": "0.15%",
        "sponsor_name": "VictoryShares",
        "sponsor_url": "https://www.vcm.com/products/etfs/qqqn",
        "quick_take": "QQQN holds the next 100 emerging Nasdaq innovators — the companies on the verge of graduating to the Nasdaq-100. It's a bet on tomorrow's tech leaders today.",
        "bluf": "The <strong>VictoryShares Nasdaq Next 50 ETF (QQQN)</strong> — also known as the 'Q Next' — tracks the Nasdaq Next Generation 100 Index, which holds the 101st through 200th largest Nasdaq non-financial stocks. Think of it as the farm team for the Nasdaq-100: the emerging companies that could become the next Apple or NVIDIA. Higher growth potential, higher risk.",
        "overview_title": "QQQN Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>QQQN</strong> gives you exposure to mid-cap Nasdaq innovators that have outgrown the small-cap world but haven't yet earned a spot in QQQ's elite Nasdaq-100. These are companies in hypergrowth phases — biotech breakthroughs, next-gen software, disruptive retail, emerging semiconductors.</p>
        <p>Why investors are drawn to QQQN:</p>
        <ul>
            <li><strong>Tomorrow's Leaders Today:</strong> Catch companies before they become massive — when the growth curve is steepest.</li>
            <li><strong>Natural "Graduation" Effect:</strong> When these companies grow large enough, they get promoted to the Nasdaq-100 — often triggering price appreciation.</li>
            <li><strong>Diversified Innovation:</strong> 100 companies across biotech, software, fintech, and consumer tech.</li>
        </ul>
        <p>It's a higher-risk, higher-reward complement to QQQ or QQQM — not a replacement.</p>""",
        "pros": [
            ("Access to High-Growth Emerging Companies", "Exposure to the next wave of Nasdaq innovators before they become household names."),
            ("'Graduation' Upside", "Companies promoted to the Nasdaq-100 often see institutional buying that boosts prices."),
            ("Low Cost", "0.15% expense ratio — reasonable for a growth-focused thematic ETF."),
            ("Diversified Across 100 Holdings", "Not a single-stock bet — 100 companies spread across tech, biotech, and consumer sectors."),
        ],
        "cons": [
            ("Higher Volatility", "Mid-cap growth companies swing harder in both directions than the mega-caps in QQQ."),
            ("Less Proven Track Record", "Newer ETF with shorter history than QQQ — less data on how it performs across market cycles."),
            ("Smaller Companies = More Risk", "Some holdings are early-stage with unproven profitability — higher failure risk."),
            ("Lower Liquidity", "Less trading volume than QQQ/QQQM — slightly wider bid-ask spreads."),
        ],
        "personas": [
            ("fa-telescope", "The Future-Spotter", "You want to own the companies that will be in QQQ 5 years from now — while they're still affordable and growing fast."),
            ("fa-dumbbell", "The Aggressive Growth Investor", "You've maxed out on VOO and QQQ and want even more growth exposure. QQQN is your next tier."),
            ("fa-puzzle-piece", "The Portfolio Diversifier", "You want small/mid-cap Nasdaq innovation to complement your large-cap heavy portfolio."),
        ],
        "scenarios": [
            ("Catching the Next NVIDIA", "A semiconductor company in QQQN's holdings delivers a breakthrough. It gets promoted to the Nasdaq-100, triggering massive institutional buying — and your QQQN position benefits from the surge."),
            ("Biotech Boom", "A wave of FDA approvals hits multiple QQQN biotech holdings simultaneously — the fund surges far more than QQQ because of the smaller, more reactive companies it holds."),
        ],
        "comp1_ticker": "QQQ",
        "comp1_name": "Invesco QQQ Trust",
        "comp1_hold": "Nasdaq-100 (top 100)",
        "comp1_why": "The established Nasdaq giants. QQQ is lower risk than QQQN — mega-caps vs. mid-caps.",
        "comp2_ticker": "IJH",
        "comp2_name": "iShares Core S&P Mid-Cap ETF",
        "comp2_hold": "S&P Mid-Cap 400",
        "comp2_why": "Broader mid-cap exposure not limited to Nasdaq — more diversified but less tech-innovation focused.",
        "verdict": "QQQN is for investors who believe the best Nasdaq returns come from catching companies on the rise — before they become giants. It's a smart <em>satellite</em> holding alongside QQQ or QQQM, adding growth torque to a portfolio. <strong>Don't go all-in; use it as a calculated growth booster.</strong>",
        "verdict_cta": "<strong>Add QQQN alongside QQQ/QQQM for a complete Nasdaq growth stack — future leaders plus current champions.</strong>",
    },

    "ivv": {
        "name": "IVV — iShares Core S&P 500 ETF",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / S&P 500 Index",
        "frequency": "Quarterly",
        "expense": "0.03%",
        "sponsor_name": "iShares (BlackRock)",
        "sponsor_url": "https://www.ishares.com/us/products/239726/ishares-core-sp-500-etf",
        "quick_take": "IVV is BlackRock's gold-standard S&P 500 ETF — same index as VOO and SPY at minimal cost, with the world's largest asset manager behind it.",
        "bluf": "The <strong>iShares Core S&P 500 ETF (IVV)</strong> tracks the S&P 500 at the same ultra-low 0.03% cost as Vanguard's VOO. Managed by BlackRock — the world's largest asset manager with over $10 trillion under management — IVV is the preferred S&P 500 vehicle for Fidelity and many institutional accounts. Same index, same cost, exceptional execution.",
        "overview_title": "IVV Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>IVV</strong> is one of the three dominant S&P 500 ETFs alongside VOO and SPY. At 0.03%, it's tied for cheapest alongside VOO, making it a top-tier choice for cost-conscious long-term investors.</p>
        <p>Why investors choose IVV:</p>
        <ul>
            <li><strong>Tied for Lowest Cost:</strong> 0.03% — matches VOO exactly, and far cheaper than SPY's 0.09%.</li>
            <li><strong>BlackRock Backing:</strong> The world's largest and most reputable asset manager — rock-solid operations and governance.</li>
            <li><strong>Fidelity-Friendly:</strong> Often the default S&P 500 choice for Fidelity brokerage accounts.</li>
            <li><strong>Strong Liquidity:</strong> One of the most actively traded ETFs, with institutional-grade execution.</li>
        </ul>
        <p>Whether you pick VOO, SPY, or IVV is largely a matter of brokerage preference — the investment itself is essentially identical.</p>""",
        "pros": [
            ("Ultra-Low 0.03% Cost", "Tied with VOO for cheapest S&P 500 ETF — your returns stay in your pocket."),
            ("BlackRock's Scale and Stability", "Backed by the world's largest asset manager — industry-leading risk management and operations."),
            ("Same S&P 500 Exposure", "500 largest U.S. companies — the classic diversified American equity portfolio."),
            ("Strong Liquidity", "Highly liquid with institutional-grade trading efficiency."),
        ],
        "cons": [
            ("No Differentiation from Competitors", "Effectively identical to VOO — choice comes down to brokerage preference, not investment merit."),
            ("Market Risk", "Follows the S&P 500 — declines with broad market selloffs."),
            ("Low Dividend Yield", "~1.3% yield — not suitable for income-focused strategies."),
            ("U.S.-Only Exposure", "No international diversification built in."),
        ],
        "personas": [
            ("fa-university", "The Fidelity Customer", "You primarily use Fidelity. IVV integrates seamlessly and is often the default S&P 500 selection — same great outcome as VOO."),
            ("fa-balance-scale", "The Diversified Core Builder", "You want the S&P 500 as your portfolio foundation. IVV, VOO, SPY — pick any, sleep well."),
            ("fa-landmark", "The Institutional Mirror Investor", "You want to invest alongside the world's largest funds. BlackRock's IVV is their standard S&P 500 tool."),
        ],
        "scenarios": [
            ("Fidelity 401(k) Simplicity", "Your Fidelity workplace plan offers IVV. You pick it as your core equity holding and contribute automatically — the simplest path to market returns."),
            ("Tax-Loss Harvesting Pair", "You hold VOO but want to harvest a tax loss in a down market. You sell VOO and immediately buy IVV — same exposure, different ETF, no wash-sale issue."),
        ],
        "comp1_ticker": "VOO",
        "comp1_name": "Vanguard S&P 500 ETF",
        "comp1_hold": "S&P 500 Index",
        "comp1_why": "Functionally identical at the same 0.03% cost. VOO preferred by Vanguard account holders; choice is personal preference.",
        "comp2_ticker": "SPY",
        "comp2_name": "SPDR S&P 500 ETF Trust",
        "comp2_hold": "S&P 500 Index",
        "comp2_why": "3x the cost (0.09%) but maximum liquidity for traders. IVV is better for long-term investors.",
        "verdict": "IVV is an excellent choice — tied for cheapest, backed by BlackRock, and perfectly tracking the S&P 500. For Fidelity users or BlackRock fans, <strong>IVV is the natural choice</strong>. For everyone else, it's a dead heat with VOO.",
        "verdict_cta": "<strong>VOO, SPY, or IVV — just pick one and start investing. Any of the three will serve you well for decades.</strong>",
    },

    "dia": {
        "name": "DIA — SPDR Dow Jones Industrial Average ETF Trust",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / Dow Jones Industrial Average",
        "frequency": "Monthly",
        "expense": "0.16%",
        "sponsor_name": "State Street (SSGA)",
        "sponsor_url": "https://www.ssga.com/us/en/individual/etfs/funds/spdr-dow-jones-industrial-average-etf-trust-dia",
        "quick_take": "DIA is 'The Dow' in ETF form — 30 of America's most iconic blue-chip companies, paying monthly dividends.",
        "bluf": "The <strong>SPDR Dow Jones Industrial Average ETF Trust (DIA)</strong> — nicknamed 'the Diamonds' — tracks the 30 companies that make up the famous Dow Jones Industrial Average. These are America's most storied corporations: Apple, Goldman Sachs, McDonald's, Boeing, Visa, Johnson & Johnson. It's a concentrated portfolio of blue-chip royalty, paying monthly dividends.",
        "overview_title": "DIA Explained: What It Is and Why It Matters",
        "overview_body": """<p>The Dow Jones Industrial Average is the most-cited market index in the world, but it's often misunderstood. It's price-weighted (not market-cap weighted) and holds only 30 stocks — making it far more concentrated than the S&P 500 or Nasdaq-100.</p>
        <p>Why investors own DIA:</p>
        <ul>
            <li><strong>Blue-Chip Stability:</strong> Only the most established U.S. companies — proven business models with decades of history.</li>
            <li><strong>Monthly Dividends:</strong> DIA pays dividends monthly, unlike most index ETFs that pay quarterly.</li>
            <li><strong>Lower Tech Concentration:</strong> More balanced sector exposure than QQQ — including industrials, financials, and consumer staples.</li>
            <li><strong>Iconic Benchmark:</strong> Tracking "the Dow" connects you to the most widely recognized financial indicator in the world.</li>
        </ul>""",
        "pros": [
            ("Monthly Dividend Payments", "One of the few index ETFs paying monthly — great for income-focused investors managing cash flow."),
            ("Blue-Chip Quality", "Only 30 of the most established, financially sound American companies."),
            ("Lower Volatility Than Nasdaq", "More balanced sector mix reduces the sharp swings seen in tech-heavy ETFs."),
            ("Iconic, Well-Understood Index", "The Dow is the world's most recognized market gauge — simple story to explain."),
        ],
        "cons": [
            ("Only 30 Stocks", "Extremely concentrated — a single company's problems can meaningfully impact the fund."),
            ("Price-Weighted Oddity", "Higher-priced stocks carry more weight regardless of company size — an unusual and somewhat arbitrary methodology."),
            ("Higher Cost Than S&P 500 ETFs", "0.16% vs 0.03% for VOO — six times more expensive for less diversification."),
            ("Underperforms vs S&P 500 Long-Term", "Historically, the Dow has trailed the broader S&P 500 over long periods."),
        ],
        "personas": [
            ("fa-flag-usa", "The Blue-Chip Loyalist", "You want only America's most established, brand-name companies. The Dow's 30 icons give you exactly that."),
            ("fa-money-bill-wave", "The Monthly Income Investor", "You need monthly cash flow from your investments. DIA's monthly dividend schedule fits perfectly."),
            ("fa-tv", "The 'I Watch the News' Investor", "You follow the Dow on the news every day and want your portfolio to mirror what you're tracking. DIA makes that connection real."),
        ],
        "scenarios": [
            ("Monthly Cash Flow Planning", "You're retired and prefer monthly income to manage your budget. DIA's monthly dividend schedule aligns with your monthly expenses better than quarterly-paying funds."),
            ("Economic Sensitivity Play", "You believe the U.S. industrial and financial economy is strengthening. DIA's heavy weighting in financials (Goldman, JPMorgan) and industrials gives you direct exposure."),
        ],
        "comp1_ticker": "VOO",
        "comp1_name": "Vanguard S&P 500 ETF",
        "comp1_hold": "S&P 500 (500 stocks)",
        "comp1_why": "More diversified (500 vs 30 stocks), cheaper (0.03%), and stronger historical performance. Better for most investors.",
        "comp2_ticker": "DDM",
        "comp2_name": "ProShares Ultra Dow30",
        "comp2_hold": "2x leveraged Dow Jones",
        "comp2_why": "For aggressive investors wanting 2x daily Dow exposure. Much higher risk — not for buy-and-hold.",
        "verdict": "DIA is a solid, blue-chip ETF with the unique appeal of monthly dividends and iconic brand recognition. But its 30-stock concentration and price-weighting methodology make it inferior to the S&P 500 for most long-term investors. <strong>Best as a complement, not a core holding.</strong>",
        "verdict_cta": "<strong>Love the Dow? Own DIA. Want the best long-term returns? Pair it with VOO.</strong>",
    },

    "djd": {
        "name": "DJD — Invesco Dow Jones Industrial Average Dividend ETF",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Dividend ETF",
        "strategy": "Dividend-Weighted Dow Jones",
        "frequency": "Monthly",
        "expense": "0.07%",
        "sponsor_name": "Invesco",
        "sponsor_url": "https://www.invesco.com/us/financial-products/etfs/product-detail?ticker=DJD",
        "quick_take": "DJD takes the Dow's 30 iconic blue chips and reweights them by dividend yield — giving income investors more of what they want: higher-yielding blue chips.",
        "bluf": "The <strong>Invesco Dow Jones Industrial Average Dividend ETF (DJD)</strong> holds the same 30 Dow companies as DIA, but instead of weighting by stock price, it weights by dividend yield. Companies paying higher dividends get larger allocations. The result: a higher-yielding, income-tilted version of the Dow, paying monthly dividends at a very competitive 0.07% cost.",
        "overview_title": "DJD Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>DJD</strong> is the dividend investor's version of the Dow. By tilting toward higher-yielding Dow components, it naturally overweights sectors like financials, energy, and industrials — and underweights low-yielders like high-growth tech names.</p>
        <p>Why DJD stands out:</p>
        <ul>
            <li><strong>Higher Yield Than DIA:</strong> Dividend weighting produces a meaningfully higher yield than price-weighted DIA.</li>
            <li><strong>Low Cost:</strong> 0.07% — significantly cheaper than DIA's 0.16% for similar blue-chip exposure.</li>
            <li><strong>Monthly Income:</strong> Pays dividends monthly — ideal for income-focused portfolios.</li>
            <li><strong>Quality Floor:</strong> Still only Dow components — America's most established companies.</li>
        </ul>""",
        "pros": [
            ("Higher Dividend Yield Than DIA", "Dividend-weighting boosts yield — you get more income from the same 30 blue-chip companies."),
            ("Very Low Cost", "At 0.07%, much cheaper than DIA (0.16%) for similar underlying exposure."),
            ("Monthly Income Payments", "Monthly dividends for smooth, predictable cash flow management."),
            ("Blue-Chip Quality", "Still the same 30 Dow stalwarts — proven, established, financially sound companies."),
        ],
        "cons": [
            ("Only 30 Stocks", "Concentrated in just 30 companies — sector tilts can be significant."),
            ("Lower Growth Potential", "Dividend weighting underweights high-growth low-payout names like tech leaders."),
            ("Dow Methodology Quirks", "Inherits the Dow's unusual price-weighted base before the dividend re-weighting."),
            ("Less Known / Less Liquid", "Smaller fund than DIA — wider bid-ask spreads, less institutional coverage."),
        ],
        "personas": [
            ("fa-hand-holding-usd", "The Blue-Chip Income Seeker", "You love the Dow's quality but want more income. DJD tilts the same 30 companies toward higher payers — best of both worlds."),
            ("fa-calendar-alt", "The Monthly Cash Flow Planner", "You need monthly income to cover expenses. DJD's monthly dividends align perfectly with regular financial needs."),
            ("fa-piggy-bank", "The Cost-Conscious Dow Investor", "You want Dow exposure but found DIA expensive at 0.16%. DJD gives you more yield for less fee."),
        ],
        "scenarios": [
            ("Income Upgrade From DIA", "You own DIA and learn DJD pays higher dividends at lower cost for the same underlying stocks. You switch to DJD and immediately improve your income-per-dollar-invested ratio."),
            ("Retirement Income Portfolio", "You build a core monthly income portfolio with DJD, SCHD, and AGG — blue-chip dividends, dividend growth, and bond income — covering all bases."),
        ],
        "comp1_ticker": "DIA",
        "comp1_name": "SPDR Dow Jones Industrial Average ETF",
        "comp1_hold": "Price-weighted Dow Jones 30",
        "comp1_why": "The standard Dow ETF — more liquid, longer history. DJD wins on yield and cost.",
        "comp2_ticker": "SCHD",
        "comp2_name": "Schwab U.S. Dividend Equity ETF",
        "comp2_hold": "High-quality U.S. dividend stocks",
        "comp2_why": "Broader dividend strategy (100 stocks) with stronger dividend growth focus. Better diversification than DJD.",
        "verdict": "DJD is a smart upgrade over DIA for income-focused investors — same blue-chip quality, higher yield, lower cost. It's not a top-tier dividend ETF compared to SCHD, but within the Dow universe, <strong>DJD is the better income choice.</strong>",
        "verdict_cta": "<strong>If you want the Dow with better income and lower fees — DJD beats DIA head-to-head.</strong>",
    },

    "ddm": {
        "name": "DDM — ProShares Ultra Dow30",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Leveraged Equity ETF",
        "strategy": "2x Daily Leverage / Dow Jones Industrial Average",
        "frequency": "Quarterly",
        "expense": "0.95%",
        "sponsor_name": "ProShares",
        "sponsor_url": "https://www.proshares.com/our-etfs/leveraged-and-inverse/ddm/",
        "quick_take": "DDM delivers 2x the daily return of the Dow Jones — amplifying both gains and losses. It's a tactical tool for experienced traders, not a buy-and-hold investment.",
        "bluf": "The <strong>ProShares Ultra Dow30 (DDM)</strong> seeks daily investment results that correspond to 2x (200%) the performance of the Dow Jones Industrial Average. On a day when the Dow goes up 1%, DDM aims to go up 2%. And when the Dow drops 1%, DDM drops 2%. This amplification makes DDM powerful for short-term tactical bets — and dangerous for the unprepared.",
        "overview_title": "DDM Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>DDM</strong> is a leveraged ETF — it uses financial derivatives to amplify the Dow's daily returns. This is critical: the 2x leverage is reset <em>daily</em>, which creates a phenomenon called volatility decay over time. Holding leveraged ETFs long-term almost always underperforms the underlying index.</p>
        <p>Key facts about DDM:</p>
        <ul>
            <li><strong>2x Daily Leverage:</strong> Doubles the Dow's daily up/down moves.</li>
            <li><strong>Volatility Decay:</strong> Daily rebalancing causes long-term underperformance in sideways or volatile markets.</li>
            <li><strong>Tactical Tool:</strong> Best used for short-term directional bets (days to weeks), not long-term investing.</li>
            <li><strong>High Cost:</strong> 0.95% expense ratio — over 30x more expensive than VOO.</li>
        </ul>
        <p><strong>⚠️ Warning:</strong> DDM is not suitable for most investors. It can rapidly lose value in volatile markets even if the Dow ends the period roughly flat.</p>""",
        "pros": [
            ("Amplified Upside in Trending Markets", "In a strong bull run, DDM can nearly double the Dow's gains — excellent short-term tactical weapon."),
            ("Highly Liquid", "Actively traded with tight spreads — easy in and out for tactical positions."),
            ("Simple Dow Leverage", "Straightforward product based on the world's most recognized index."),
            ("Potential Hedge Tool", "Advanced investors can use leveraged ETFs to offset other portfolio exposures."),
        ],
        "cons": [
            ("Volatility Decay Destroys Long-Term Returns", "Daily rebalancing causes compounding losses in sideways/volatile markets — DDM is NOT for buy-and-hold."),
            ("Very High Expense Ratio", "0.95% annual cost — over 30x more expensive than VOO."),
            ("Amplified Losses", "The Dow drops 2%? DDM drops 4%. Rapid drawdowns can be severe."),
            ("Complex Tax Treatment", "Frequent derivatives trading creates tax complexity — not for simple passive investing."),
        ],
        "personas": [
            ("fa-chess", "The Tactical Trader", "You've studied leveraged ETFs, understand the decay risk, and want short-term amplified exposure to a Dow rally. You're in and out within days or weeks."),
            ("fa-shield-alt", "The Portfolio Hedger", "You have a short Dow position elsewhere and use DDM to fine-tune your net exposure. Advanced risk management only."),
            ("fa-ban", "NOT for Buy-and-Hold Investors", "If you're planning to hold for months or years, DDM is the wrong tool. The math works against you over time."),
        ],
        "scenarios": [
            ("Short-Term Dow Breakout Play", "Technical analysis shows the Dow breaking to new highs with strong momentum. You buy DDM for a 1–2 week hold to amplify the move, then exit with your profit before decay accumulates."),
            ("Avoiding DDM's Trap", "You bought DDM planning to hold for a year. The Dow finished +10% but you lost money — because volatility along the way triggered daily decay. This scenario is why DDM requires careful, short-term use."),
        ],
        "comp1_ticker": "DIA",
        "comp1_name": "SPDR Dow Jones Industrial Average ETF",
        "comp1_hold": "1x Dow Jones (no leverage)",
        "comp1_why": "The safe version — same Dow exposure without leverage risk. Appropriate for all investors.",
        "comp2_ticker": "UDOW",
        "comp2_name": "ProShares UltraPro Dow30",
        "comp2_hold": "3x Daily Leverage / Dow Jones",
        "comp2_why": "Even more aggressive — 3x leverage for traders who want maximum amplification with maximum risk.",
        "verdict": "DDM is a specialized tactical instrument for experienced traders — not a passive investment. Used correctly in short-term, trending markets, it can amplify returns. <strong>Used incorrectly by long-term investors, it destroys capital.</strong> Know what you own.",
        "verdict_cta": "<strong>Only trade DDM if you understand leverage decay. When in doubt — own DIA instead.</strong>",
    },

    "fdn": {
        "name": "FDN — First Trust Dow Jones Internet Index Fund",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Sector Equity ETF",
        "strategy": "Internet & Technology Companies",
        "frequency": "Annually",
        "expense": "0.51%",
        "sponsor_name": "First Trust",
        "sponsor_url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FDN",
        "quick_take": "FDN is a concentrated bet on the internet economy — major platforms, e-commerce, streaming, and digital advertising. Think Amazon, Meta, Netflix, Salesforce.",
        "bluf": "The <strong>First Trust Dow Jones Internet Index Fund (FDN)</strong> tracks the Dow Jones Internet Composite Index — a collection of the largest and most liquid U.S.-listed internet companies. Amazon, Meta, Netflix, Alphabet, Salesforce, PayPal — the companies that built and dominate the digital economy. It's a thematic bet on the internet's continued dominance.",
        "overview_title": "FDN Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>FDN</strong> was launched in 2006 and has served as a proxy for investing in the internet economy before that was a common concept. It focuses on companies that derive a majority of their revenue from internet-based activities.</p>
        <p>Why investors choose FDN:</p>
        <ul>
            <li><strong>Pure Internet Play:</strong> More focused on internet business models than QQQ, which includes non-internet tech like semiconductors and enterprise software.</li>
            <li><strong>E-Commerce + Advertising + Streaming:</strong> Covers the major internet monetization models in one fund.</li>
            <li><strong>Long Track Record:</strong> 15+ years of internet sector performance data.</li>
        </ul>
        <p><strong>Note:</strong> FDN is more expensive (0.51%) and concentrated than broad market ETFs — it's a satellite holding, not a core position.</p>""",
        "pros": [
            ("Targeted Internet Economy Exposure", "Pure play on the digital economy — e-commerce, social media, streaming, SaaS."),
            ("Long Track Record", "15+ years of data showing performance through multiple market cycles including the 2008 crash and 2020 pandemic."),
            ("Includes Mega-Cap Anchors", "Amazon, Alphabet, Meta provide large-cap stability alongside higher-growth names."),
            ("Sector Leadership", "Internet companies continue to take market share across nearly every industry."),
        ],
        "cons": [
            ("High Expense Ratio", "0.51% — expensive compared to QQQ (0.20%) or VOO (0.03%)."),
            ("Concentrated Holdings", "Top holdings can represent 30–40% of the fund — significant single-stock risk."),
            ("High Correlation to QQQ", "Much of what FDN holds overlaps with QQQ — may not add as much diversification as expected."),
            ("Minimal Dividends", "Internet companies reinvest aggressively — FDN pays dividends only annually and at very low yield."),
        ],
        "personas": [
            ("fa-globe", "The Digital Economy Believer", "You see the internet economy taking over every traditional industry and want pure-play exposure beyond what QQQ offers."),
            ("fa-shopping-cart", "The E-Commerce Bull", "Amazon and the shift to online retail is a generational trend you want to own. FDN puts it front and center."),
            ("fa-chart-line", "The QQQ Supplement Seeker", "You own QQQ but want even more tilted internet/e-commerce weighting in your growth allocation."),
        ],
        "scenarios": [
            ("Digital Ad Cycle Play", "Meta and Alphabet report blowout ad revenue as the digital advertising market rebounds. FDN's heavy weighting in both names amplifies the sector tailwind."),
            ("E-Commerce Peak Season", "Holiday shopping season drives massive Amazon and e-commerce sales. FDN's internet-commerce heavy portfolio participates directly."),
        ],
        "comp1_ticker": "QQQ",
        "comp1_name": "Invesco QQQ Trust",
        "comp1_hold": "Nasdaq-100 (broader tech)",
        "comp1_why": "Lower cost (0.20%) with broader tech exposure including semiconductors. More diversified, more liquid.",
        "comp2_ticker": "OGIG",
        "comp2_name": "O'Shares Global Internet Giants ETF",
        "comp2_hold": "Global internet leaders",
        "comp2_why": "Adds international internet exposure (Tencent, Alibaba, etc.) that FDN lacks — more global reach.",
        "verdict": "FDN makes sense as a concentrated satellite position for investors who believe specifically in the internet economy and want more focused exposure than QQQ provides. <strong>Just don't overpay for overlap — check your QQQ holdings before adding FDN.</strong>",
        "verdict_cta": "<strong>If internet leadership is your thesis, FDN delivers. Use it as a 5–15% satellite position, not a core holding.</strong>",
    },

    "swppx": {
        "name": "SWPPX — Schwab S&P 500 Index Fund",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index Mutual Fund",
        "strategy": "Passive / S&P 500 Index",
        "frequency": "Quarterly",
        "expense": "0.02%",
        "sponsor_name": "Charles Schwab",
        "sponsor_url": "https://www.schwab.com/research/mutual-funds/quotes/fees/swppx",
        "quick_take": "SWPPX is Schwab's S&P 500 index fund — the cheapest way to own the S&P 500, period. 0.02% expense ratio with no minimums and no transaction fees at Schwab.",
        "bluf": "The <strong>Schwab S&P 500 Index Fund (SWPPX)</strong> is technically a mutual fund (not an ETF), but it's the gold standard for Schwab account holders. At 0.02%, it's the cheapest S&P 500 vehicle available anywhere — cheaper even than VOO at 0.03%. No minimum investment, no transaction fees, automatic investment friendly, and same S&P 500 exposure.",
        "overview_title": "SWPPX Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>SWPPX</strong> is a mutual fund version of the S&P 500 index — meaning it's priced once per day at the closing NAV rather than trading throughout the day like an ETF. For long-term investors who don't need intraday trading, this is completely irrelevant. What matters is the 0.02% cost — the absolute lowest S&P 500 expense ratio available.</p>
        <p>Why Schwab customers love SWPPX:</p>
        <ul>
            <li><strong>Cheapest S&P 500 Available:</strong> 0.02% — beats VOO (0.03%), IVV (0.03%), and SPY (0.09%).</li>
            <li><strong>No Transaction Fees at Schwab:</strong> Buy and sell with zero commissions.</li>
            <li><strong>Automatic Investment:</strong> Unlike ETFs, you can set up automatic investing in exact dollar amounts (not shares).</li>
            <li><strong>No Minimum Investment:</strong> Start with $1 if you want.</li>
        </ul>""",
        "pros": [
            ("Absolute Lowest Cost", "0.02% — the cheapest S&P 500 product in existence. Every basis point saved is returns kept."),
            ("No Transaction Fees at Schwab", "Zero commissions — buy and sell freely without paying per-trade costs."),
            ("Dollar-Amount Auto-Investing", "Set up automatic $X/month contributions — no need to calculate shares."),
            ("No Minimum Investment", "Start with any amount — removes all barriers to entry."),
        ],
        "cons": [
            ("Mutual Fund, Not ETF", "Priced once daily at market close — no intraday trading ability."),
            ("Schwab Ecosystem Only", "No transaction-fee-free access at other brokerages — best if you're already a Schwab customer."),
            ("No Options Market", "Can't sell covered calls or buy puts on a mutual fund — for options strategies, use SPY or VOO."),
            ("Less Flexible for Tax-Loss Harvesting", "Mutual funds have slightly more complex tax-loss harvesting mechanics vs. ETFs."),
        ],
        "personas": [
            ("fa-university", "The Schwab Account Holder", "You use Schwab and want the absolute lowest cost S&P 500 exposure available. SWPPX is your answer — period."),
            ("fa-robot", "The Automatic Investor", "You want to automate a fixed monthly dollar amount into the S&P 500. SWPPX's mutual fund structure makes this trivial."),
            ("fa-child", "The New Investor", "Zero minimums and zero fees make SWPPX the perfect starting point for anyone new to investing at Schwab."),
        ],
        "scenarios": [
            ("Automated Retirement Savings", "You set up a $400/month automatic investment into SWPPX in your Schwab IRA. Every month, dollar-cost averaging buys you more S&P 500 at the lowest possible cost — no thinking required."),
            ("401(k) Core Holding", "Your Schwab 401(k) plan offers SWPPX as an option. You allocate 70% of contributions here — automatic S&P 500 diversification at industry-minimum cost."),
        ],
        "comp1_ticker": "VOO",
        "comp1_name": "Vanguard S&P 500 ETF",
        "comp1_hold": "S&P 500 Index (ETF)",
        "comp1_why": "ETF version at 0.03% — slightly more expensive but tradeable intraday and available everywhere.",
        "comp2_ticker": "FXAIX",
        "comp2_name": "Fidelity 500 Index Fund",
        "comp2_hold": "S&P 500 Index (Mutual Fund)",
        "comp2_why": "Fidelity's equivalent at the same 0.015% — use SWPPX at Schwab, FXAIX at Fidelity.",
        "verdict": "If you're a Schwab customer, SWPPX is the single best S&P 500 product available — cheaper than any ETF, zero friction, automatic investing. <strong>Use it. It's the closest thing to free investing in the S&P 500 that exists.</strong>",
        "verdict_cta": "<strong>Schwab account + SWPPX + monthly automatic investment = the simplest wealth-building machine available.</strong>",
    },

    "itot": {
        "name": "ITOT — iShares Core S&P Total U.S. Stock Market ETF",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / Total U.S. Stock Market",
        "frequency": "Quarterly",
        "expense": "0.03%",
        "sponsor_name": "iShares (BlackRock)",
        "sponsor_url": "https://www.ishares.com/us/products/239724/ishares-core-sp-total-us-stock-market-etf",
        "quick_take": "ITOT captures the entire U.S. stock market — not just the S&P 500's 500 largest, but all 3,500+ investable American companies. The broadest possible U.S. equity exposure at zero-fee cost.",
        "bluf": "The <strong>iShares Core S&P Total U.S. Stock Market ETF (ITOT)</strong> is a true total market fund — holding over 3,500 U.S. stocks from large-caps down to small-caps. While the S&P 500 captures 80% of U.S. market value, ITOT gets you the other 20% too: the mid-caps and small-caps with their potential for faster growth. At 0.03%, it's the broadest possible bet on American capitalism.",
        "overview_title": "ITOT Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>ITOT</strong> tracks the S&P Total Market Index — encompassing large, mid, small, and micro-cap U.S. stocks. In practice, the largest companies still dominate (Apple, Microsoft, NVIDIA), but you also own thousands of smaller companies that VOO misses.</p>
        <p>Why ITOT appeals to investors:</p>
        <ul>
            <li><strong>Complete U.S. Coverage:</strong> 3,500+ stocks — if it's publicly traded in the U.S., ITOT likely owns it.</li>
            <li><strong>Small-Cap Upside:</strong> Small and mid-caps historically outperform large-caps over very long periods.</li>
            <li><strong>Same Ultra-Low Cost as VOO:</strong> 0.03% — no premium for the extra coverage.</li>
            <li><strong>True Diversification:</strong> Not dependent on any single sector or market segment's performance.</li>
        </ul>""",
        "pros": [
            ("Broadest Possible U.S. Diversification", "3,500+ companies — every investable U.S. stock in one ETF."),
            ("Small & Mid-Cap Upside", "Captures faster-growing smaller companies that S&P 500 ETFs miss."),
            ("Ultra-Low Cost", "0.03% — same as VOO despite holding 7x more stocks."),
            ("Truly Passive 'Own Everything' Approach", "Perfect for investors who believe markets are efficient and want total exposure."),
        ],
        "cons": [
            ("Large-Caps Still Dominate", "Despite 3,500+ holdings, the top 10 stocks still represent ~25% of the fund — similar to VOO in practice."),
            ("Minimal Return Difference from VOO", "Historically, ITOT and VOO have nearly identical returns — the small-cap addition barely moves the needle."),
            ("Quarterly Dividends Only", "Same modest yield as other broad market ETFs — not for income-focused strategies."),
            ("Slight Complexity vs. S&P 500 Story", "Harder to explain than 'I own the S&P 500' — though functionally nearly identical."),
        ],
        "personas": [
            ("fa-globe-americas", "The Total Market Purist", "You believe in owning everything — every company, every size — and letting the market decide winners. ITOT is your vehicle."),
            ("fa-seedling", "The Small-Cap Exposure Seeker", "You want VOO-style broad exposure but with a bit of small-cap upside included. ITOT adds it seamlessly."),
            ("fa-infinity", "The 'Own America Forever' Investor", "You want the simplest possible long-term investment. ITOT = all of America's public companies. Done."),
        ],
        "scenarios": [
            ("One-Fund Portfolio", "You want simplicity: one ETF, total U.S. market, hold forever. ITOT does it — 3,500+ companies, minimum cost, automatic rebalancing."),
            ("Complementing International ETFs", "You build a global portfolio: 60% ITOT (U.S.) + 40% VXUS (international) = the entire world's stock market at near-zero cost."),
        ],
        "comp1_ticker": "VTI",
        "comp1_name": "Vanguard Total Stock Market ETF",
        "comp1_hold": "Total U.S. stock market",
        "comp1_why": "Vanguard's version of the same concept — nearly identical to ITOT at 0.03%. Preference depends on brokerage."),
        "comp2_ticker": "VOO",
        "comp2_name": "Vanguard S&P 500 ETF",
        "comp2_hold": "S&P 500 (500 largest stocks)",
        "comp2_why": "500-stock focus vs. 3,500+. ITOT adds small/mid-cap coverage; VOO is simpler S&P 500 story.",
        "verdict": "ITOT is the definitive 'own everything American' ETF. For investors who want the broadest possible U.S. equity exposure at minimum cost, <strong>ITOT is as complete as it gets.</strong> The difference from VOO is small but real — and for the same 0.03%, why not own everything?",
        "verdict_cta": "<strong>ITOT: the simplest, most comprehensive, cheapest way to own the entire U.S. stock market.</strong>",
    },

    "eps": {
        "name": "EPS — WisdomTree U.S. LargeCap Fund",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Earnings-Weighted Large Cap",
        "frequency": "Quarterly",
        "expense": "0.08%",
        "sponsor_name": "WisdomTree",
        "sponsor_url": "https://www.wisdomtree.com/investments/etfs/equity/eps",
        "quick_take": "EPS weights S&P 500-like large caps by their earnings — not market cap. Companies that earn more get bigger allocations, potentially reducing overvaluation risk.",
        "bluf": "The <strong>WisdomTree U.S. LargeCap Fund (EPS)</strong> takes a fresh approach to large-cap investing: instead of weighting by market cap (like VOO), it weights by earnings power. Companies generating the most profit get the biggest portfolio share — regardless of whether the market has bid up their valuations. The result is a value-tilted, fundamentally-weighted alternative to the S&P 500.",
        "overview_title": "EPS Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>EPS</strong> stands for earnings per share — and that's exactly what drives this ETF's construction. Companies are selected from large-cap U.S. stocks and weighted by their annual earnings, rewarding the most profitable businesses with the largest portfolio weight.</p>
        <p>Why EPS is worth considering:</p>
        <ul>
            <li><strong>Fundamentals-Based Weighting:</strong> Reduces overexposure to overvalued stocks that have high prices but not necessarily high earnings.</li>
            <li><strong>Value Tilt:</strong> Naturally tilts toward profitable, value-oriented companies — a classic factor that has historically added returns.</li>
            <li><strong>Low Cost:</strong> At 0.08%, reasonably priced for an actively-constructed factor ETF.</li>
            <li><strong>Different from S&P 500:</strong> Provides genuine portfolio differentiation from market-cap-weighted funds.</li>
        </ul>""",
        "pros": [
            ("Earnings-Weighted = Fundamentally Sound", "Portfolio weight driven by actual profitability — reduces exposure to overpriced momentum stocks."),
            ("Value Factor Exposure", "Historically, value stocks have outperformed growth over long periods — EPS tilts toward this."),
            ("Reasonable Cost", "0.08% — competitive for a smart-beta / factor ETF."),
            ("Large-Cap Quality Screen", "Still focuses on established, large-cap companies — not chasing micro-cap speculation."),
        ],
        "cons": [
            ("Underperforms in Growth Bull Markets", "When high-valuation growth stocks (like NVIDIA) lead the market, earnings-weighting underweights them — you miss the best of the rally."),
            ("Less Familiar Story", "Harder to explain than 'I own the S&P 500' — earnings weighting is a more nuanced concept."),
            ("Lower Liquidity Than S&P 500 ETFs", "Less actively traded — wider spreads, less institutional attention."),
            ("Factor Risk: Value Can Underperform", "Value factors can underperform for extended periods (see 2010–2020 growth dominance)."),
        ],
        "personas": [
            ("fa-calculator", "The Value-Conscious Investor", "You worry that the S&P 500 is too weighted toward expensive tech stocks. EPS rebalances toward what companies actually earn."),
            ("fa-balance-scale", "The Smart-Beta Explorer", "You understand factor investing and want to tilt your large-cap allocation toward earnings quality and value."),
            ("fa-diversify", "The S&P 500 Diversifier", "You hold VOO as core and want something different — EPS provides genuine non-correlated large-cap exposure."),
        ],
        "scenarios": [
            ("Tech Valuation Bubble Hedge", "Tech stocks trade at extreme P/E multiples. EPS's earnings weighting naturally reduces exposure to the most expensive names, cushioning the blow if valuations compress."),
            ("Steady Profit Machine Environments", "In a period where steady, profitable companies outperform growth stories, EPS's earnings-weighted approach generates alpha vs. standard market-cap ETFs."),
        ],
        "comp1_ticker": "VOO",
        "comp1_name": "Vanguard S&P 500 ETF",
        "comp1_hold": "Market-cap weighted S&P 500",
        "comp1_why": "The standard — cheaper (0.03%), more liquid, simpler. VOO is better for most investors as core holding.",
        "comp2_ticker": "SCHV",
        "comp2_name": "Schwab U.S. Large-Cap Value ETF",
        "comp2_hold": "Large-cap value stocks",
        "comp2_why": "Pure value tilt vs. EPS's earnings weighting — similar value exposure through different methodology.",
        "verdict": "EPS is an interesting smart-beta alternative to market-cap weighted S&P 500 ETFs. Its earnings weighting makes fundamental sense — you own what companies earn, not what the market thinks they're worth. <strong>Best as a portfolio complement rather than a complete S&P 500 replacement.</strong>",
        "verdict_cta": "<strong>Consider EPS as a value-tilted satellite alongside VOO — diversifying across market approaches, not just individual stocks.</strong>",
    },

    "schb": {
        "name": "SCHB — Schwab U.S. Broad Market ETF",
        "eyebrow": "Index ETFs",
        "category": "index",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / Total U.S. Stock Market",
        "frequency": "Quarterly",
        "expense": "0.03%",
        "sponsor_name": "Charles Schwab",
        "sponsor_url": "https://www.schwab.com/etfs/schwab-etfs/schb",
        "quick_take": "SCHB is Schwab's total U.S. market ETF — covering 2,500+ American stocks at the absolute minimum cost. The Schwab customer's best one-fund equity solution.",
        "bluf": "The <strong>Schwab U.S. Broad Market ETF (SCHB)</strong> tracks the Dow Jones U.S. Broad Stock Market Index — holding approximately 2,500 U.S. stocks from mega-cap to small-cap. At 0.03%, it competes directly with Vanguard's VTI and iShares' ITOT. For Schwab customers, SCHB is the natural choice for total U.S. market exposure with no additional friction.",
        "overview_title": "SCHB Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>SCHB</strong> represents the broad sweep of U.S. equity markets — from Apple and Microsoft at the top to smaller companies driving innovation at the bottom. It's Schwab's answer to VTI: same concept, same cost, same simplicity.</p>
        <p>Why SCHB makes sense:</p>
        <ul>
            <li><strong>Total U.S. Market:</strong> ~2,500 stocks covering large, mid, and small-cap companies.</li>
            <li><strong>Zero-Cost Equivalent:</strong> 0.03% — tied for cheapest broad market ETF.</li>
            <li><strong>No-Fee Trading at Schwab:</strong> Zero commission at Schwab — no friction to buying more.</li>
            <li><strong>Simplicity:</strong> One fund. All of America. Done.</li>
        </ul>""",
        "pros": [
            ("Covers the Entire U.S. Market", "2,500+ stocks — all major, mid, and small-cap U.S. companies in one fund."),
            ("Tied for Absolute Lowest Cost", "0.03% — no ETF does U.S. broad market cheaper."),
            ("No Fees at Schwab", "Zero-commission trading at Charles Schwab — buy as often as you want."),
            ("Simple and Powerful", "One fund covers the entire investable U.S. stock universe."),
        ],
        "cons": [
            ("Large-Caps Dominate Despite Breadth", "Despite 2,500+ holdings, the fund behaves similarly to VOO — mega-caps dominate by market cap."),
            ("Schwab-Ecosystem Advantage Only", "Best for Schwab customers — no particular advantage elsewhere."),
            ("Minimal Dividend Yield", "Total market ETFs yield ~1.3% — not for income-focused strategies."),
            ("Nearly Identical to VTI/ITOT", "If you already hold VTI or ITOT, SCHB adds nothing — perfect substitutes."),
        ],
        "personas": [
            ("fa-university", "The Schwab Loyalist", "You manage your investments at Schwab and want the best total-market ETF available with zero commission friction. SCHB is it."),
            ("fa-bullseye", "The One-Fund Investor", "You want one equity ETF that covers all of America and costs virtually nothing. SCHB checks every box."),
            ("fa-seedling", "The Beginner Building Wealth", "You're starting your investment journey and want the simplest possible approach: buy SCHB regularly, hold forever."),
        ],
        "scenarios": [
            ("Schwab IRA Simplicity", "You open a Schwab Roth IRA and pick SCHB as your single holding. Every month you buy more. In 30 years, you've participated in the entire U.S. stock market's growth at effectively zero cost."),
            ("Tax-Loss Harvest Pair", "You hold VTI in a taxable account. Markets dip. You sell VTI for a tax loss and immediately buy SCHB — same exposure, different fund, no wash-sale violation."),
        ],
        "comp1_ticker": "VTI",
        "comp1_name": "Vanguard Total Stock Market ETF",
        "comp1_hold": "Total U.S. market (4,000+ stocks)",
        "comp1_why": "Vanguard's version — slightly more holdings but functionally identical. Choose by brokerage preference."),
        "comp2_ticker": "ITOT",
        "comp2_name": "iShares Core S&P Total U.S. Stock Market ETF",
        "comp2_hold": "Total U.S. market (3,500+ stocks)",
        "comp2_why": "BlackRock's version — same concept at same cost. Choose based on your brokerage of choice.",
        "verdict": "SCHB is one of the best ETFs ever created — maximum diversification, minimum cost, zero complexity. <strong>For Schwab customers, this is the obvious choice.</strong> For everyone else, it's equally excellent — just pick the version that matches your brokerage.",
        "verdict_cta": "<strong>SCHB: America's companies. Your portfolio. Zero cost. Just buy it.</strong>",
    },
}

# Dividend ETFs data
DIVIDEND_ETF_DATA = {
    "schd": {
        "name": "SCHD — Schwab U.S. Dividend Equity ETF",
        "eyebrow": "Dividend ETFs",
        "category": "dividend",
        "asset_class": "Dividend Equity ETF",
        "strategy": "High Dividend + Dividend Growth",
        "frequency": "Quarterly",
        "expense": "0.06%",
        "sponsor_name": "Charles Schwab",
        "sponsor_url": "https://www.schwab.com/etfs/schwab-etfs/schd",
        "quick_take": "SCHD is widely regarded as the best dividend ETF in existence — exceptional yield, strong dividend growth, rock-bottom cost, and a quality screen that keeps garbage out.",
        "bluf": "The <strong>Schwab U.S. Dividend Equity ETF (SCHD)</strong> is the dividend investor's dream: ~3.5% yield, 10%+ annual dividend growth history, only 0.06% cost, and a rigorous quality screen that selects the best 100 dividend-paying U.S. companies. It doesn't just pay you now — it pays you <em>more</em> every year. SCHD is the gold standard for dividend growth investing.",
        "overview_title": "SCHD Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>SCHD</strong> tracks the Dow Jones U.S. Dividend 100 Index, which selects stocks based on four criteria: cash flow to total debt, return on equity, dividend yield relative to peers, and 5-year dividend growth rate. The result is a portfolio of financially strong companies that consistently grow their dividends.</p>
        <p>Why SCHD is so beloved:</p>
        <ul>
            <li><strong>High & Growing Yield:</strong> ~3.5% current yield that has grown 10%+ annually — doubling every 7 years.</li>
            <li><strong>Quality Screen:</strong> Only financially healthy companies make the cut — strong balance sheets, not just high yields.</li>
            <li><strong>Ultra-Low Cost:</strong> 0.06% — remarkable for an actively-screened dividend strategy.</li>
            <li><strong>Value Tilt:</strong> SCHD naturally tilts toward value stocks, providing diversification from growth-heavy VOO/QQQ.</li>
        </ul>""",
        "pros": [
            ("Best-in-Class Yield + Growth Combination", "~3.5% yield growing 10%+ annually — compounding income machine. Dividend doubles every ~7 years."),
            ("Strict Quality Screen", "Only financially sound companies with sustained dividend growth — not yield traps."),
            ("Ultra-Low 0.06% Cost", "Extraordinary value for a dividend quality strategy."),
            ("Value Diversification", "Complements growth-heavy VOO/QQQ with value-sector exposure."),
        ],
        "cons": [
            ("No Tech Exposure", "SCHD's quality screen excludes most tech companies — you miss the Mag 7's capital appreciation."),
            ("Quarterly Dividends", "Pays quarterly — not monthly like some income-focused alternatives."),
            ("U.S. Only", "No international dividend exposure — global income seekers need additional ETFs."),
            ("Underperforms in Tech Bull Markets", "When tech dominates, SCHD's value tilt lags. Patience required."),
        ],
        "personas": [
            ("fa-chart-line", "The Dividend Growth Investor", "You want income that grows faster than inflation. SCHD's 10%+ annual dividend growth means your income doubles every 7 years."),
            ("fa-home", "The Near-Retiree", "You're building a portfolio that will pay you in retirement. SCHD's growing income stream lets you live off dividends without selling shares."),
            ("fa-balance-scale", "The VOO Complement Seeker", "You hold VOO for growth but want income and value exposure. SCHD + VOO is one of the most popular portfolio combinations for good reason."),
        ],
        "scenarios": [
            ("The Dividend Snowball", "You invest $1,000/month into SCHD for 25 years, reinvesting all dividends. The combination of price appreciation, yield, and 10% annual dividend growth creates a snowball that eventually generates $30,000+/year in passive income."),
            ("Retirement Income Switch", "At retirement, you stop reinvesting SCHD dividends and start spending them. Your 3.5% yield on a $500,000 position generates $17,500/year — and growing — without touching the principal."),
        ],
        "comp1_ticker": "VYM",
        "comp1_name": "Vanguard High Dividend Yield ETF",
        "comp1_hold": "U.S. high dividend stocks",
        "comp1_why": "Higher yield than SCHD but lower dividend growth. VYM is for immediate income; SCHD is for growing income.",
        "comp2_ticker": "DGRO",
        "comp2_name": "iShares Core Dividend Growth ETF",
        "comp2_hold": "U.S. dividend growth stocks",
        "comp2_why": "Lower yield but includes tech dividend growers. More growth-oriented than SCHD.",
        "verdict": "SCHD is the closest thing to a perfect dividend ETF that exists. High quality, high yield, high growth, low cost. <strong>If you own one dividend ETF, make it SCHD.</strong>",
        "verdict_cta": "<strong>SCHD + VOO + time = one of the most powerful long-term portfolio combinations available to retail investors.</strong>",
    },

    "jepi": {
        "name": "JEPI — JPMorgan Equity Premium Income ETF",
        "eyebrow": "Dividend ETFs",
        "category": "dividend",
        "asset_class": "Covered Call / Income ETF",
        "strategy": "Equity + ELN Covered Call Income",
        "frequency": "Monthly",
        "expense": "0.35%",
        "sponsor_name": "JPMorgan Asset Management",
        "sponsor_url": "https://am.jpmorgan.com/us/en/asset-management/adv/products/jpmorgan-equity-premium-income-etf-etf-shares-46641q761",
        "quick_take": "JEPI delivers high monthly income (~7-8% yield) by selling options on S&P 500 stocks. It caps your upside in bull markets but provides exceptional income with lower volatility than SPY.",
        "bluf": "The <strong>JPMorgan Equity Premium Income ETF (JEPI)</strong> is one of the most innovative income products ever created. It holds a defensive equity portfolio and sells equity-linked notes (ELNs) based on S&P 500 call options to generate a high monthly income stream. The result: ~7-8% yield paid monthly, with roughly 30% less volatility than the S&P 500. It's not a growth fund — it's an income machine.",
        "overview_title": "JEPI Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>JEPI</strong> uses a two-part strategy: (1) a defensive equity portfolio of lower-volatility S&P 500 stocks managed by JPMorgan's experts, and (2) selling out-of-the-money S&P 500 call options via ELNs to generate premium income. That options premium becomes monthly income distributed to shareholders.</p>
        <p>Why income investors are drawn to JEPI:</p>
        <ul>
            <li><strong>~7-8% Monthly Yield:</strong> High income paid every month — excellent for retirees and income-focused investors.</li>
            <li><strong>Lower Volatility:</strong> Defensive stock selection + option selling dampens portfolio swings.</li>
            <li><strong>Monthly Payments:</strong> 12 dividend payments per year vs. quarterly for most ETFs.</li>
            <li><strong>JPMorgan Quality:</strong> Managed by one of the world's premier asset managers with active stock selection.</li>
        </ul>
        <p><strong>Trade-off:</strong> In strong bull markets, JEPI significantly underperforms the S&P 500. The options capping is intentional — you're trading growth for income.</p>""",
        "pros": [
            ("High Monthly Income (~7-8%)", "Exceptional yield paid monthly — one of the highest sustainable income ETFs available."),
            ("Lower Volatility Than S&P 500", "Defensive positioning reduces drawdowns — smoother ride than pure equity ETFs."),
            ("Active Stock Selection Quality", "JPMorgan's team actively selects defensive, quality stocks — not passive index garbage."),
            ("Perfect for Retirement Income", "Monthly high yield with capital preservation focus — designed for living off investments."),
        ],
        "cons": [
            ("Capped Upside in Bull Markets", "When stocks surge, JEPI lags badly — call options cap gains. In 2023, JEPI significantly underperformed SPY."),
            ("Variable Yield", "The ~7-8% yield changes monthly based on options market conditions — not a fixed payment."),
            ("Higher Cost", "0.35% — more expensive than passive ETFs, though reasonable for an actively managed strategy."),
            ("Return of Capital Risk", "Some distributions may include return of capital, which can affect tax treatment."),
        ],
        "personas": [
            ("fa-money-bill-wave", "The Income Retiree", "You need 6-8% annual income from your investments to fund retirement. JEPI's monthly checks match your cash flow needs perfectly."),
            ("fa-umbrella", "The Low-Volatility Seeker", "You want equity-like income without equity-like volatility. JEPI's defensive approach gives you a smoother portfolio experience."),
            ("fa-calendar-alt", "The Monthly Budget Planner", "Your monthly expenses are predictable. JEPI's monthly income aligns perfectly with your budget — 12 payments a year."),
        ],
        "scenarios": [
            ("Retirement Income Portfolio", "You convert $400,000 of your retirement portfolio to JEPI. At 7% yield, you receive ~$2,333/month in income — without touching your principal — while the portfolio's defensive character protects from large drawdowns."),
            ("Income + Growth Portfolio Split", "You split your portfolio: 60% VOO (growth), 40% JEPI (income). VOO provides long-term appreciation; JEPI provides monthly cash flow. The combination balances your need for both."),
        ],
        "comp1_ticker": "JEPQ",
        "comp1_name": "JPMorgan Nasdaq Equity Premium Income ETF",
        "comp1_hold": "Nasdaq-100 + options income",
        "comp1_why": "JEPI's sibling — same strategy but on Nasdaq-100. Higher income potential, higher volatility, more tech-focused."),
        "comp2_ticker": "DIVO",
        "comp2_name": "Amplify CWP Enhanced Dividend Income ETF",
        "comp2_hold": "Dividend stocks + covered calls",
        "comp2_why": "Similar income strategy — covered calls on dividend stocks. More selective portfolio, slightly lower yield than JEPI.",
        "verdict": "JEPI is the premier monthly income ETF for investors who prioritize cash flow over capital appreciation. If you need the income and can accept lower growth in bull markets, <strong>JEPI delivers exceptional value.</strong> Combine with a growth ETF like VOO for a complete portfolio.",
        "verdict_cta": "<strong>Need monthly income? JEPI is the premium solution — high yield, JPMorgan quality, monthly checks.</strong>",
    },

    "vym": {
        "name": "VYM — Vanguard High Dividend Yield ETF",
        "eyebrow": "Dividend ETFs",
        "category": "dividend",
        "asset_class": "Dividend Equity ETF",
        "strategy": "High Dividend Yield",
        "frequency": "Quarterly",
        "expense": "0.06%",
        "sponsor_name": "Vanguard",
        "sponsor_url": "https://investor.vanguard.com/etf/profile/VYM",
        "quick_take": "VYM is Vanguard's high dividend ETF — 400+ stocks with above-average yields, at 0.06% cost. Excellent for income investors who want Vanguard's reliability and breadth.",
        "bluf": "The <strong>Vanguard High Dividend Yield ETF (VYM)</strong> holds 400+ U.S. stocks forecasted to pay above-average dividends. It's broader than SCHD (400 stocks vs 100), slightly lower yield, but covers more ground. At Vanguard's signature 0.06% cost, VYM is a workhorse dividend fund for income and stability.",
        "overview_title": "VYM Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>VYM</strong> tracks the FTSE High Dividend Yield Index — selecting U.S. stocks forecasted to have above-average dividend yields. With 400+ holdings, it's significantly more diversified than SCHD's 100-stock focused approach.</p>
        <p>Why VYM works for dividend investors:</p>
        <ul>
            <li><strong>~3% Yield:</strong> Meaningfully above S&P 500 (~1.5%) while maintaining diversification.</li>
            <li><strong>400+ Holdings:</strong> More diversified than SCHD — less concentration risk.</li>
            <li><strong>Vanguard Trustworthiness:</strong> The pioneer of low-cost investing behind this ETF — world-class execution.</li>
            <li><strong>Value + Income:</strong> Natural tilt toward financials, healthcare, and consumer staples — sectors that pay reliable dividends.</li>
        </ul>""",
        "pros": [
            ("Broader Diversification Than SCHD", "400+ holdings vs SCHD's 100 — less concentrated, smoother ride."),
            ("~3% Above-Average Yield", "Meaningfully higher than S&P 500 yield with broad diversification."),
            ("Vanguard's Ultra-Low 0.06% Cost", "Same expense ratio as SCHD — excellent value for an income strategy."),
            ("Reliable Quarterly Income", "Consistent quarterly dividends from established, profitable companies."),
        ],
        "cons": [
            ("Lower Yield & Growth vs SCHD", "SCHD typically offers higher yield AND faster dividend growth — making VYM the second choice for most dividend investors."),
            ("Includes More Mediocre Dividend Payers", "With 400+ stocks, quality screening is looser — includes companies that may cut dividends."),
            ("Slower Dividend Growth", "VYM prioritizes current yield over growth rate — dividend growth lags SCHD over time."),
            ("Value Trap Risk", "High-yield stocks can be value traps — companies with high yields because their prices have fallen."),
        ],
        "personas": [
            ("fa-balance-scale", "The Diversified Income Investor", "You want dividend income but prefer broader diversification than SCHD's 100-stock focus. VYM's 400+ holdings give you more cushion."),
            ("fa-hand-holding-usd", "The Yield-Focused Retiree", "You need income now (not growth) and want a trustworthy, well-diversified source. VYM delivers reliably."),
            ("fa-university", "The Vanguard Loyalist", "You manage everything at Vanguard and want their take on dividend investing. VYM is the natural choice."),
        ],
        "scenarios": [
            ("Income Portfolio Alongside VOO", "You split retirement savings 70% VOO / 30% VYM. VOO drives long-term growth; VYM provides current income to cover expenses without selling your growth position."),
            ("Dividend Income Reinvestment", "You reinvest VYM dividends for 20 years. The quarterly compounding — 400+ dividend-paying companies — builds substantial wealth while maintaining portfolio stability."),
        ],
        "comp1_ticker": "SCHD",
        "comp1_name": "Schwab U.S. Dividend Equity ETF",
        "comp1_hold": "100 high-quality dividend stocks",
        "comp1_why": "Higher yield AND faster growth than VYM — better total return for most dividend investors. VYM wins on diversification breadth.",
        "comp2_ticker": "HDV",
        "comp2_name": "iShares Core High Dividend ETF",
        "comp2_hold": "75 high-yield U.S. stocks",
        "comp2_why": "Higher yield than VYM but only 75 stocks — more concentrated, higher risk.",
        "verdict": "VYM is a solid, reliable dividend ETF — the 'safe and steady' choice from the most trusted name in indexing. For income investors who prefer breadth over concentration, <strong>VYM is excellent.</strong> For those wanting the best total return from dividends, SCHD has the edge.",
        "verdict_cta": "<strong>Vanguard + dividends + low cost = VYM. Hard to go wrong with this one.</strong>",
    },

    "vig": {
        "name": "VIG — Vanguard Dividend Appreciation ETF",
        "eyebrow": "Dividend ETFs",
        "category": "dividend",
        "asset_class": "Dividend Growth ETF",
        "strategy": "Dividend Growth / 10+ Year Growers",
        "frequency": "Quarterly",
        "expense": "0.06%",
        "sponsor_name": "Vanguard",
        "sponsor_url": "https://investor.vanguard.com/etf/profile/VIG",
        "quick_take": "VIG only holds companies with 10+ consecutive years of dividend growth. It's lower yield than VYM or SCHD, but offers exceptional long-term dividend compounding from elite, proven growers.",
        "bluf": "The <strong>Vanguard Dividend Appreciation ETF (VIG)</strong> tracks companies with at least 10 consecutive years of dividend growth. These aren't just high-yield stocks — they're financially elite companies that have raised their dividends through recessions, crises, and market crashes. Lower yield today, but maximum compounding tomorrow.",
        "overview_title": "VIG Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>VIG</strong> tracks the S&P U.S. Dividend Growers Index — companies that have grown their dividends for at least 10 consecutive years. The result is a portfolio heavy with Dividend Aristocrats and elite blue chips: Microsoft, Apple, Visa, JPMorgan, UnitedHealth Group.</p>
        <p>Why VIG's approach creates long-term wealth:</p>
        <ul>
            <li><strong>Quality Floor:</strong> Only companies that have grown dividends through recessions qualify — the ultimate stress test of financial health.</li>
            <li><strong>Compounding Dividend Growth:</strong> 10%+ annual dividend growth means income doubles every 7 years — wealth creation engine.</li>
            <li><strong>Lower Volatility:</strong> Dividend growers tend to be financially stable companies that hold up better in downturns.</li>
            <li><strong>Tech Included:</strong> Unlike pure value dividend ETFs, VIG includes tech dividend growers — Microsoft, Apple, Broadcom.</li>
        </ul>""",
        "pros": [
            ("Only Elite Dividend Growers", "10+ year consecutive dividend growth requirement — the most stringent quality screen."),
            ("Includes Tech Dividend Leaders", "Microsoft, Apple, and Broadcom qualify — growth + dividends in one fund."),
            ("Lower Volatility Than S&P 500", "Financial stability of consistent dividend growers = smoother portfolio performance."),
            ("Ultra-Low 0.06% Cost", "Vanguard's signature pricing — remarkable for a quality-screened strategy."),
        ],
        "cons": [
            ("Lower Current Yield (~1.7%)", "Quality over yield — VIG yields less than SCHD (~3.5%) or VYM (~3%). Not ideal for immediate income needs."),
            ("Patience Required", "The compounding story takes time — VIG shines over decades, not years."),
            ("Can't Rely on Income for Expenses", "Low current yield means you can't replace a paycheck with VIG dividends immediately."),
            ("Less Income Focus Than Peers", "Investors who prioritize current income will be disappointed by the low yield."),
        ],
        "personas": [
            ("fa-seedling", "The Long-Term Compounder", "You're 20–40 years from retirement and want income that will be substantial by the time you need it. VIG's 10%+ growth rate is your jet fuel."),
            ("fa-shield-alt", "The Quality Equity Investor", "You want to hold the most financially sound companies in the market — the ones that have proven they can grow dividends through any environment."),
            ("fa-calendar-check", "The Patience Investor", "You understand that VIG's low yield today becomes exceptional income 20 years from now. You're playing the long game."),
        ],
        "scenarios": [
            ("The 30-Year Income Doubling Machine", "You invest $100,000 in VIG at age 35. It currently yields 1.7%, paying $1,700/year. But at 10% annual dividend growth, by age 65 your yield on original cost exceeds 30% — paying $30,000+/year from the same $100,000 investment."),
            ("Portfolio Stability in a Downturn", "Markets crash 40%. VIG's dividend-growth companies maintain and raise their dividends. Their financial strength shows — VIG drops less than the S&P 500 and recovers faster."),
        ],
        "comp1_ticker": "SCHD",
        "comp1_name": "Schwab U.S. Dividend Equity ETF",
        "comp1_hold": "100 high-quality dividend stocks",
        "comp1_why": "Higher current yield (~3.5%) with strong growth. SCHD is better for near-term income needs; VIG better for ultra-long-term compounding.",
        "comp2_ticker": "NOBL",
        "comp2_name": "ProShares S&P 500 Dividend Aristocrats ETF",
        "comp2_hold": "S&P 500 Dividend Aristocrats (25+ yr growers)",
        "comp2_why": "Even more stringent 25-year growth requirement than VIG's 10 years — more concentrated in proven blue chips.",
        "verdict": "VIG is for patient investors building generational income. The low current yield is intentional — you're planting seeds. The harvest comes in decades of compounding at 10%+ growth rates. <strong>If your investment horizon is 20+ years, VIG's compounding power is extraordinary.</strong>",
        "verdict_cta": "<strong>Think long term. Buy VIG. Reinvest. Wait. The math will reward you more than you expect.</strong>",
    },

    "voo_div": {  # voo in dividend folder
        "_file": "voo.html",
        "name": "VOO — Vanguard S&P 500 ETF",
        "eyebrow": "Index ETFs",
        "category": "dividend",
        "asset_class": "Equity Index ETF",
        "strategy": "Passive / S&P 500 Index",
        "frequency": "Quarterly",
        "expense": "0.03%",
        "sponsor_name": "Vanguard",
        "sponsor_url": "https://investor.vanguard.com/etf/profile/VOO",
        "quick_take": "VOO is the gold-standard S&P 500 ETF — ultra-cheap, tax-efficient, and the core holding for millions of long-term investors.",
        "bluf": "The <strong>Vanguard S&P 500 ETF (VOO)</strong> is about as simple and powerful as investing gets. It owns a slice of every company in the S&P 500 — the 500 largest U.S. businesses — at a cost so low it's practically free. For most normal investors, VOO *is* the portfolio.",
        "overview_title": "VOO Explained: What It Is and Why It Matters",
        "overview_body": """<p><strong>VOO</strong> tracks the S&P 500 Index — 500 leading American companies including Apple, Microsoft, Amazon, NVIDIA, and more. When the U.S. economy does well, VOO does well.</p>
        <ul>
            <li><strong>Near-Zero Cost:</strong> At 0.03%, you keep almost every dollar of return the market produces.</li>
            <li><strong>Broad Diversification:</strong> 500 companies across all major sectors.</li>
            <li><strong>Long-Term Track Record:</strong> ~10% average annual return historically.</li>
        </ul>""",
        "pros": [
            ("Lowest Cost in Class", "0.03% expense ratio — essentially free to own."),
            ("Instant 500-Stock Diversification", "One purchase gives you the entire S&P 500."),
            ("Proven Long-Term Performance", "~10% average annual returns historically."),
            ("Tax Efficiency", "Vanguard's patent-protected structure minimizes capital gains distributions."),
        ],
        "cons": [
            ("U.S. Only Exposure", "No international diversification."),
            ("Market Risk", "Can drop 30–50% in recessions."),
            ("Quarterly Dividends Only", "Dividend yield is modest (~1.3–1.5%)."),
            ("No Small Cap Exposure", "Only large-cap stocks."),
        ],
        "personas": [
            ("fa-seedling", "The Long-Term Wealth Builder", "You're in your 20s–40s and just want to grow wealth over decades without thinking about it."),
            ("fa-home", "The 'Set It & Forget It' Investor", "You don't want to research stocks. One ETF, buy regularly, hold forever."),
            ("fa-chart-line", "The Core Portfolio Builder", "You need a reliable equity foundation for a diversified portfolio."),
        ],
        "scenarios": [
            ("Dollar-Cost Averaging", "$500/month for 30 years at historical returns grows to over $1 million."),
            ("Riding Out a Crash", "VOO drops 35%. You keep buying — history shows S&P 500 always recovers to new highs."),
        ],
        "comp1_ticker": "SPY",
        "comp1_name": "SPDR S&P 500 ETF Trust",
        "comp1_hold": "S&P 500 Index",
        "comp1_why": "Same index, more liquid for traders. VOO better for long-term holds due to lower cost.",
        "comp2_ticker": "IVV",
        "comp2_name": "iShares Core S&P 500 ETF",
        "comp2_hold": "S&P 500 Index",
        "comp2_why": "BlackRock's version at same 0.03% cost. Nearly identical.",
        "verdict": "VOO is the single best investment for the average long-term investor. Cheap, diversified, historically powerful. <strong>If you own nothing else, own VOO.</strong>",
        "verdict_cta": "<strong>Buy VOO, hold it forever, and let compounding do its magic.</strong>",
    },
}

# Add remaining dividend ETFs with generic templates
GENERIC_DIVIDEND_ETFS = {
    "agg": {"name": "AGG", "full": "iShares Core U.S. Aggregate Bond ETF", "type": "bond", "asset": "Bond", "strategy": "Total Bond Market", "freq": "Monthly", "exp": "0.03%", "sponsor": "iShares", "url": "https://www.ishares.com/us/products/239458"},
    "cgdv": {"name": "CGDV", "full": "Capital Group Dividend Value ETF", "type": "dividend quality", "asset": "Dividend Equity", "strategy": "Dividend Value", "freq": "Quarterly", "exp": "0.33%", "sponsor": "Capital Group", "url": "https://www.capitalgroup.com/individual/investments/fund/cgdv"},
    "cowz": {"name": "COWZ", "full": "Pacer US Cash Cows 100 ETF", "type": "free cash flow", "asset": "Equity", "strategy": "Free Cash Flow Screen", "freq": "Quarterly", "exp": "0.49%", "sponsor": "Pacer", "url": "https://www.paceretfs.com/products/cowz"},
    "ddm": {"name": "DDM", "full": "ProShares Ultra Dow30", "type": "leveraged", "asset": "Leveraged Equity", "strategy": "2x Dow Jones Daily", "freq": "Quarterly", "exp": "0.95%", "sponsor": "ProShares", "url": "https://www.proshares.com/our-etfs/leveraged-and-inverse/ddm/"},
    "des": {"name": "DES", "full": "WisdomTree U.S. SmallCap Dividend Fund", "type": "small cap dividend", "asset": "Small Cap Dividend Equity", "strategy": "Small Cap Dividend", "freq": "Monthly", "exp": "0.38%", "sponsor": "WisdomTree", "url": "https://www.wisdomtree.com/investments/etfs/equity/des"},
    "dgro": {"name": "DGRO", "full": "iShares Core Dividend Growth ETF", "type": "dividend growth", "asset": "Dividend Growth Equity", "strategy": "Dividend Growth", "freq": "Quarterly", "exp": "0.08%", "sponsor": "iShares", "url": "https://www.ishares.com/us/products/272822"},
    "dgrw": {"name": "DGRW", "full": "WisdomTree U.S. Quality Dividend Growth Fund", "type": "quality dividend growth", "asset": "Quality Dividend Growth", "strategy": "Quality + Dividend Growth", "freq": "Monthly", "exp": "0.28%", "sponsor": "WisdomTree", "url": "https://www.wisdomtree.com/investments/etfs/equity/dgrw"},
    "dia": {"name": "DIA", "full": "SPDR Dow Jones Industrial Average ETF", "type": "blue chip", "asset": "Equity Index", "strategy": "Dow Jones Industrial Average", "freq": "Monthly", "exp": "0.16%", "sponsor": "SSGA", "url": "https://www.ssga.com/us/en/individual/etfs/funds/spdr-dow-jones-industrial-average-etf-trust-dia"},
    "divo": {"name": "DIVO", "full": "Amplify CWP Enhanced Dividend Income ETF", "type": "covered call dividend", "asset": "Enhanced Income", "strategy": "Dividend + Covered Calls", "freq": "Monthly", "exp": "0.55%", "sponsor": "Amplify", "url": "https://amplifyetfs.com/divo"},
    "djd": {"name": "DJD", "full": "Invesco Dow Jones Industrial Average Dividend ETF", "type": "dividend dow", "asset": "Dividend Blue Chip", "strategy": "Dividend-Weighted Dow Jones", "freq": "Monthly", "exp": "0.07%", "sponsor": "Invesco", "url": "https://www.invesco.com/us/financial-products/etfs/product-detail?ticker=DJD"},
    "dln": {"name": "DLN", "full": "WisdomTree U.S. LargeCap Dividend Fund", "type": "large cap dividend", "asset": "Large Cap Dividend", "strategy": "Dividend-Weighted Large Cap", "freq": "Monthly", "exp": "0.28%", "sponsor": "WisdomTree", "url": "https://www.wisdomtree.com/investments/etfs/equity/dln"},
    "don": {"name": "DON", "full": "WisdomTree U.S. MidCap Dividend Fund", "type": "mid cap dividend", "asset": "Mid Cap Dividend", "strategy": "Dividend-Weighted Mid Cap", "freq": "Monthly", "exp": "0.38%", "sponsor": "WisdomTree", "url": "https://www.wisdomtree.com/investments/etfs/equity/don"},
    "dvy": {"name": "DVY", "full": "iShares Select Dividend ETF", "type": "high dividend", "asset": "High Dividend Equity", "strategy": "High Dividend Select", "freq": "Quarterly", "exp": "0.38%", "sponsor": "iShares", "url": "https://www.ishares.com/us/products/239464"},
    "fcfy": {"name": "FCFY", "full": "First Trust S&P 500 Diversified Free Cash Flow ETF", "type": "free cash flow", "asset": "Quality Equity", "strategy": "Free Cash Flow Focus", "freq": "Quarterly", "exp": "0.39%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FCFY"},
    "fdl": {"name": "FDL", "full": "First Trust Morningstar Dividend Leaders Index Fund", "type": "dividend leaders", "asset": "Dividend Quality Equity", "strategy": "Dividend Leaders", "freq": "Monthly", "exp": "0.45%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FDL"},
    "fdn": {"name": "FDN", "full": "First Trust Dow Jones Internet Index Fund", "type": "internet", "asset": "Internet Sector Equity", "strategy": "Internet Companies", "freq": "Annually", "exp": "0.51%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FDN"},
    "fthi": {"name": "FTHI", "full": "First Trust BuyWrite Income ETF", "type": "covered call income", "asset": "Enhanced Income", "strategy": "S&P 500 BuyWrite", "freq": "Monthly", "exp": "0.85%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FTHI"},
    "ftqi": {"name": "FTQI", "full": "First Trust Nasdaq BuyWrite Income ETF", "type": "nasdaq covered call", "asset": "Enhanced Income", "strategy": "Nasdaq BuyWrite", "freq": "Monthly", "exp": "0.85%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FTQI"},
    "fvd": {"name": "FVD", "full": "First Trust Value Line Dividend Index Fund", "type": "value dividend", "asset": "Value Dividend Equity", "strategy": "Value + Dividend", "freq": "Monthly", "exp": "0.70%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FVD"},
    "hdv": {"name": "HDV", "full": "iShares Core High Dividend ETF", "type": "high dividend", "asset": "High Dividend Equity", "strategy": "High Dividend Quality", "freq": "Quarterly", "exp": "0.08%", "sponsor": "iShares", "url": "https://www.ishares.com/us/products/239551"},
    "idvo": {"name": "IDVO", "full": "Amplify International Enhanced Dividend Income ETF", "type": "intl dividend covered call", "asset": "International Enhanced Income", "strategy": "International Dividend + Covered Calls", "freq": "Monthly", "exp": "0.55%", "sponsor": "Amplify", "url": "https://amplifyetfs.com/idvo"},
    "ivv": {"name": "IVV", "full": "iShares Core S&P 500 ETF", "type": "index", "asset": "Equity Index", "strategy": "S&P 500 Index", "freq": "Quarterly", "exp": "0.03%", "sponsor": "iShares", "url": "https://www.ishares.com/us/products/239726"},
    "iwm": {"name": "IWM", "full": "iShares Russell 2000 ETF", "type": "small cap index", "asset": "Small Cap Equity", "strategy": "Russell 2000 Small Cap", "freq": "Quarterly", "exp": "0.19%", "sponsor": "iShares", "url": "https://www.ishares.com/us/products/239710"},
    "jepq": {"name": "JEPQ", "full": "JPMorgan Nasdaq Equity Premium Income ETF", "type": "nasdaq covered call income", "asset": "Enhanced Income", "strategy": "Nasdaq-100 + Options Income", "freq": "Monthly", "exp": "0.35%", "sponsor": "JPMorgan", "url": "https://am.jpmorgan.com/us/en/asset-management/adv/products/jpmorgan-nasdaq-equity-premium-income-etf"},
    "kng": {"name": "KNG", "full": "FT Cboe Vest S&P 500 Dividend Aristocrats Target Income ETF", "type": "dividend aristocrats covered call", "asset": "Enhanced Income", "strategy": "Dividend Aristocrats + Covered Calls", "freq": "Monthly", "exp": "0.75%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=KNG"},
    "kngs": {"name": "KNGS", "full": "FT Cboe Vest S&P 500 Dividend Aristocrats Target Income ETF (Similar)", "type": "dividend aristocrats income", "asset": "Enhanced Income", "strategy": "Dividend Aristocrats Target Income", "freq": "Monthly", "exp": "0.75%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/"},
    "nobl": {"name": "NOBL", "full": "ProShares S&P 500 Dividend Aristocrats ETF", "type": "dividend aristocrats", "asset": "Dividend Aristocrats Equity", "strategy": "S&P 500 Dividend Aristocrats (25+ yr growers)", "freq": "Quarterly", "exp": "0.35%", "sponsor": "ProShares", "url": "https://www.proshares.com/our-etfs/equity/nobl/"},
    "pbp": {"name": "PBP", "full": "Invesco S&P 500 BuyWrite ETF", "type": "s&p 500 covered call", "asset": "Enhanced Income", "strategy": "S&P 500 BuyWrite", "freq": "Monthly", "exp": "0.49%", "sponsor": "Invesco", "url": "https://www.invesco.com/us/financial-products/etfs/product-detail?ticker=PBP"},
    "pey": {"name": "PEY", "full": "Invesco High Yield Equity Dividend Achievers ETF", "type": "high yield dividend achievers", "asset": "High Yield Dividend", "strategy": "Dividend Achievers High Yield", "freq": "Monthly", "exp": "0.52%", "sponsor": "Invesco", "url": "https://www.invesco.com/us/financial-products/etfs/product-detail?ticker=PEY"},
    "qqew": {"name": "QQEW", "full": "First Trust NASDAQ-100 Equal Weighted Index Fund", "type": "equal weight nasdaq", "asset": "Equal Weight Tech", "strategy": "Equal-Weighted Nasdaq-100", "freq": "Quarterly", "exp": "0.58%", "sponsor": "First Trust", "url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=QQEW"},
    "qqq": {"name": "QQQ", "full": "Invesco QQQ Trust", "type": "nasdaq-100 index", "asset": "Tech Index Equity", "strategy": "Nasdaq-100 Index", "freq": "Quarterly", "exp": "0.20%", "sponsor": "Invesco", "url": "https://www.invesco.com/qqq-etf/"},
    "qqqm": {"name": "QQQM", "full": "Invesco Nasdaq-100 ETF", "type": "nasdaq-100 index", "asset": "Tech Index Equity", "strategy": "Nasdaq-100 (Buy-and-Hold Version)", "freq": "Quarterly", "exp": "0.15%", "sponsor": "Invesco", "url": "https://www.invesco.com/us/financial-products/etfs/product-detail?ticker=QQQM"},
    "qqqn": {"name": "QQQN", "full": "VictoryShares Nasdaq Next 50 ETF", "type": "nasdaq next gen", "asset": "Mid-Cap Tech", "strategy": "Nasdaq Next Generation 100", "freq": "Quarterly", "exp": "0.15%", "sponsor": "VictoryShares", "url": "https://www.vcm.com/products/etfs/qqqn"},
    "qyld": {"name": "QYLD", "full": "Global X Nasdaq 100 Covered Call ETF", "type": "nasdaq covered call high income", "asset": "Enhanced Income", "strategy": "Nasdaq-100 Covered