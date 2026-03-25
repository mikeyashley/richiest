#!/usr/bin/env python3
"""Retouch ETF pages batch 4 - insert BIL-template sections after author box."""

import re

BASE = "/Users/michael/Documents/GitHub/richiest/etfs/dividend"

ETFS = {
    "idvo": {
        "name": "Amplify International Enhanced Dividend Income ETF",
        "ticker": "IDVO",
        "exchange": "AMEX",
        "quick_take": "IDVO is best for income seekers who want international dividend exposure boosted by a covered-call overlay. It is <em>not</em> a pure-growth play.",
        "summary": "<strong>IDVO (Amplify International Enhanced Dividend Income ETF)</strong> hunts for the highest-yielding international stocks <em>and</em> layers on covered-call options to squeeze out extra premium income. Think of it as a world-income machine set to \"turbo\" — you get quarterly dividends from proven global companies, then collect bonus option premium on top. The trade-off: you cap some upside when global stocks rally hard.",
        "explained_intro": "Want juicy international dividends without flying blind into foreign markets? IDVO does the legwork for you.",
        "explained_body": "<p><strong>IDVO</strong> is an <strong>ETF</strong> that selects <strong>high-yielding international stocks</strong> (think European banks, energy majors, emerging-market giants) and then sells covered-call options on the portfolio. The option premium is added to the dividend income, resulting in a significantly higher overall yield than a plain international index fund.</p><p>Here's why investors consider IDVO:\n<ul>\n<li><strong>Enhanced Yield:</strong> Covered-call premiums stack on top of dividend income, typically pushing yield well above plain international ETFs.</li>\n<li><strong>Global Diversification:</strong> Holds companies across Europe, Asia, and emerging markets — sectors and currencies that zig when U.S. markets zag.</li>\n<li><strong>Quarterly Payments:</strong> Regular income distributions make cash-flow planning straightforward.</li>\n</ul>\n</p><p>Managed by <strong>Amplify ETFs</strong>, a boutique fund house known for income-innovation products.</p>",
        "table_row": "<td>IDVO</td><td>Equity Dividend ETF</td><td>Intl Enhanced Income (Covered Call)</td><td>Quarterly</td><td>0.70%</td><td><a href=\"https://www.amplifyetfs.com/idvo\" target=\"_blank\" rel=\"noopener noreferrer\">Amplify ETFs</a></td>",
        "pro1": "<strong>High Income Yield:</strong> Covered-call overlay boosts quarterly distributions well above a standard international dividend fund.",
        "pro2": "<strong>Global Diversification:</strong> Exposure to Europe, Asia, and EM markets that can reduce correlation to U.S. equities.",
        "pro3": "<strong>Option-Enhanced Returns:</strong> Premiums collected during flat or mildly rising markets enhance total return.",
        "pro4": "<strong>Reputable Manager:</strong> Amplify ETFs specializes in income-innovation strategies with transparent methodology.",
        "con1": "<strong>Capped Upside:</strong> Covered calls limit gains when international stocks surge — you give away the big win.",
        "con2": "<strong>Currency Risk:</strong> Foreign holdings mean your returns are affected by USD strength/weakness.",
        "con3": "<strong>Higher Fee:</strong> 0.70% expense ratio is noticeably more expensive than passive international ETFs.",
        "con4": "<strong>Complex Strategy:</strong> Options overlay adds complexity; distributions can vary quarter to quarter.",
        "persona1_icon": "fas fa-globe",
        "persona1_title": "The Global Income Hunter",
        "persona1_body": "You want income beyond U.S. borders — European dividends, Asian cash cows — but don't want the hassle of picking individual foreign stocks. IDVO bundles them with an income booster built in.",
        "persona2_icon": "fas fa-sliders-h",
        "persona2_title": "The Portfolio Diversifier",
        "persona2_body": "Your portfolio is very U.S.-heavy and you want something that moves differently. International equities plus option premium means IDVO doesn't just copy your S&P 500 ETF's moves.",
        "persona3_icon": "fas fa-hand-holding-usd",
        "persona3_title": "The Income-First Retiree",
        "persona3_body": "You need quarterly cash flow from your investments. IDVO's enhanced yield (historically above 5%) can supplement Social Security or other income streams without taking wild equity risk.",
        "scenario1_title": "Supplementing a Dividend Portfolio",
        "scenario1_body": "You already own VYM or SCHD for domestic dividends. Adding IDVO diversifies your income stream geographically — now you're collecting dividends from TotalEnergies, MUFG, and BBVA alongside your U.S. names.",
        "scenario2_title": "Filling the International Allocation",
        "scenario2_body": "Instead of a plain international index that yields under 3%, you allocate part of your \"international\" sleeve to IDVO to get paid significantly more while you wait for global markets to catch up.",
        "comp_ticker2": "IDV", "comp_name2": "iShares International Select Dividend ETF",
        "comp_ticker3": "FDD", "comp_name3": "First Trust STOXX European Select Dividend ETF",
        "comp_focus2": "High-yielding international dividend stocks, Europe-heavy", "comp_focus3": "European dividend-paying stocks only",
        "comp_strategy2": "Pure dividend screen, no options overlay", "comp_strategy3": "European dividend screen, no options",
        "comp_pick2": "Lower fee, simpler pure-dividend approach", "comp_pick3": "Pure play on European dividends",
        "verdict": "For income-focused investors willing to accept some complexity and a higher fee, <strong>IDVO delivers above-average yield with genuine global diversification.</strong> Its covered-call overlay means it shines most in sideways or moderately rising international markets. If you want the highest possible income from international stocks without worrying about picking individual names, IDVO earns its spot in the portfolio. <strong>Stop overthinking global income — IDVO packages it for you.</strong>",
    },
    "iwm": {
        "name": "iShares Russell 2000 ETF",
        "ticker": "IWM",
        "exchange": "NYSE",
        "quick_take": "IWM is best for capturing small-cap U.S. growth. It is <em>not</em> primarily an income vehicle — the yield is modest and volatility is high.",
        "summary": "<strong>IWM (iShares Russell 2000 ETF)</strong> is the go-to vehicle for owning a slice of <em>every</em> small U.S. company at once — roughly 2,000 of them. Small-cap stocks historically outperform large-caps over long periods, but the ride is bumpier. IWM lets you capture that small-company growth engine in a single, highly liquid ETF.",
        "explained_intro": "Want to own America's small businesses without picking individual stocks? IWM puts 2,000 of them in one fund.",
        "explained_body": "<p><strong>IWM</strong> tracks the <strong>Russell 2000 Index</strong>, the benchmark for U.S. small-cap stocks. These are companies typically valued between $300M and $2B — established enough to be public, small enough to have significant runway for growth.</p><p>Here's why investors consider IWM:\n<ul>\n<li><strong>Small-Cap Premium:</strong> Academic research (Fama-French) shows smaller companies have historically outperformed larger ones over long periods.</li>\n<li><strong>Domestic Focus:</strong> Small-caps earn most revenue in the U.S., meaning less exposure to global economic headwinds and foreign currency risk.</li>\n<li><strong>Deep Liquidity:</strong> IWM is one of the most actively traded ETFs on earth — easy to get in and out at tight spreads.</li>\n</ul>\n</p><p>Managed by <strong>iShares (BlackRock)</strong>, the world's largest ETF provider.</p>",
        "table_row": "<td>IWM</td><td>Equity ETF</td><td>Small-Cap Index</td><td>Quarterly</td><td>0.19%</td><td><a href=\"https://www.ishares.com/us/products/239710/ishares-russell-2000-etf\" target=\"_blank\" rel=\"noopener noreferrer\">iShares by BlackRock</a></td>",
        "pro1": "<strong>Small-Cap Growth Exposure:</strong> Access to ~2,000 U.S. small companies with higher long-run growth potential than mega-caps.",
        "pro2": "<strong>Ultra-Liquid:</strong> Massive daily volume makes IWM easy to trade with minimal slippage — used widely by institutions.",
        "pro3": "<strong>Domestically Focused:</strong> Less foreign-exchange risk versus international ETFs; benefits from U.S. economic strength.",
        "pro4": "<strong>Low Cost:</strong> 0.19% expense ratio is reasonable for a broadly diversified, high-liquidity small-cap fund.",
        "con1": "<strong>High Volatility:</strong> Small-caps swing more dramatically than large-caps — IWM can drop 20%+ in bear markets.",
        "con2": "<strong>Low Yield:</strong> Dividend yield around 1-1.5% — not a meaningful income source.",
        "con3": "<strong>Pricier Competitors:</strong> VTWO and TWOK track the same index at lower fees (0.10% vs 0.19%).",
        "con4": "<strong>Profitability Risk:</strong> Many Russell 2000 companies are unprofitable; downturns hit them disproportionately hard.",
        "persona1_icon": "fas fa-seedling",
        "persona1_title": "The Long-Term Growth Investor",
        "persona1_body": "You're investing for 10+ years and want exposure to the small-company growth premium. IWM gives you diversified access without betting everything on a handful of names.",
        "persona2_icon": "fas fa-chess-knight",
        "persona2_title": "The Tactical Trader",
        "persona2_body": "You believe the economic cycle is entering a phase that favors small-caps (falling rates, domestic stimulus) and want to position aggressively. IWM's extreme liquidity makes it the weapon of choice.",
        "persona3_icon": "fas fa-balance-scale",
        "persona3_title": "The Large-Cap Heavy Portfolio Balancer",
        "persona3_body": "Your portfolio is dominated by S&P 500 ETFs. Adding IWM diversifies your size exposure and historically reduces concentration risk in the mega-cap tech names.",
        "scenario1_title": "Riding a Small-Cap Recovery",
        "scenario1_body": "After a period where large-caps crushed small-caps, you believe the gap is due to close. You add IWM to your portfolio to capture the potential reversion — when small-caps rally, IWM tends to outperform QQQ and SPY significantly.",
        "scenario2_title": "Completing a Core-Satellite Portfolio",
        "scenario2_body": "Your core is SPY (large-cap). You add IWM as a \"satellite\" allocation (10-15%) to complete your U.S. equity coverage, giving you exposure to the full market spectrum from micro to mega.",
        "comp_ticker2": "VTWO", "comp_name2": "Vanguard Russell 2000 ETF",
        "comp_ticker3": "IJR", "comp_name3": "iShares Core S&P Small-Cap ETF",
        "comp_focus2": "Same Russell 2000 Index at lower cost", "comp_focus3": "S&P 600 small-cap index (slightly higher quality bar)",
        "comp_strategy2": "Passive index, lower fee (0.10%)", "comp_strategy3": "S&P 600 requires profitability screen",
        "comp_pick2": "Pure cost savings if you don't need IWM's liquidity", "comp_pick3": "Slightly higher quality small-caps with profitability filter",
        "verdict": "IWM is the <strong>definitive small-cap ETF</strong> — the most liquid, most recognized, most traded. For pure small-cap exposure in a U.S.-focused portfolio, IWM is hard to beat. Yes, cheaper alternatives exist, but the liquidity premium is real for active managers and traders. Long-term buy-and-hold investors might save a few basis points with VTWO, but IWM's market leadership and ecosystem make it the default. <strong>If small-cap is your game, IWM is the table.</strong>",
    },
    "kng": {
        "name": "FT Cboe Vest S&P 500 Dividend Aristocrats Target Income ETF",
        "ticker": "KNG",
        "exchange": "AMEX",
        "quick_take": "KNG is best for investors who want both dividend-aristocrat quality AND a boosted income yield via options. It is <em>not</em> for pure growth seekers.",
        "summary": "<strong>KNG (FT Cboe Vest S&P 500 Dividend Aristocrats Target Income ETF)</strong> takes the gold standard of dividend investing — S&P 500 Dividend Aristocrats (companies with 25+ years of consecutive dividend increases) — and layers on a systematic options strategy to juice the income yield well above what the dividends alone provide. You get blue-chip dividend royalty, plus option premiums deposited into your account monthly.",
        "explained_intro": "What if you could own dividend royalty AND collect extra income on top every month? That's KNG's proposition.",
        "explained_body": "<p><strong>KNG</strong> invests in the <strong>S&P 500 Dividend Aristocrats</strong> — the elite club of S&P 500 companies that have raised dividends for <strong>25+ consecutive years</strong>. Then it sells covered call options on that portfolio to generate additional income, targeting a yield significantly above the market average.</p><p>Here's why investors consider KNG:\n<ul>\n<li><strong>Dividend Aristocrat Quality:</strong> Holdings like Colgate-Palmolive, 3M, and Ecolab have raised dividends through recessions, crises, and bear markets.</li>\n<li><strong>Enhanced Income:</strong> The options overlay pushes yield to ~7-8%, far above the ~2% you'd get from the aristocrats alone.</li>\n<li><strong>Monthly Distributions:</strong> Income is paid monthly (not quarterly), making cash-flow management easier.</li>\n</ul>\n</p><p>Managed by <strong>First Trust Advisors</strong> in partnership with <strong>Cboe Vest</strong>, specialists in options-based income strategies.</p>",
        "table_row": "<td>KNG</td><td>Equity Dividend ETF</td><td>Dividend Aristocrats + Covered Call</td><td>Monthly</td><td>0.75%</td><td><a href=\"https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=KNG\" target=\"_blank\" rel=\"noopener noreferrer\">First Trust Advisors</a></td>",
        "pro1": "<strong>Premium Income (~7-8% yield):</strong> Option overlay dramatically boosts income above what dividends alone could deliver.",
        "pro2": "<strong>Battle-Tested Holdings:</strong> Dividend Aristocrats have decades of consistent dividend growth — quality is baked in.",
        "pro3": "<strong>Monthly Distributions:</strong> Paid monthly (unlike most dividend ETFs) for predictable cash-flow budgeting.",
        "pro4": "<strong>Systematic Strategy:</strong> Cboe Vest's rules-based options approach removes manager discretion and improves consistency.",
        "con1": "<strong>Upside Cap:</strong> Covered calls cap gains when Aristocrat stocks rally strongly — you participate less in big bull runs.",
        "con2": "<strong>Higher Fee:</strong> 0.75% expense ratio is significantly more than plain Aristocrat funds like NOBL (0.35%).",
        "con3": "<strong>Complex Product:</strong> Options overlay adds tax complexity (some income may be ordinary income, not qualified dividends).",
        "con4": "<strong>Sector Concentration:</strong> Aristocrats skew toward Industrials and Consumer Defensive — less tech/growth exposure.",
        "persona1_icon": "fas fa-crown",
        "persona1_title": "The Income Maximizer",
        "persona1_body": "You want the highest yield from proven, blue-chip companies. KNG's ~7-8% distribution yield is hard to match with dividend-only strategies while maintaining this level of quality.",
        "persona2_icon": "fas fa-shield-alt",
        "persona2_title": "The Conservative Retiree",
        "persona2_body": "You need reliable monthly income in retirement, prefer familiar household-name companies (Colgate, 3M, Ecolab), and can accept some growth cap in exchange for predictability.",
        "persona3_icon": "fas fa-chart-line",
        "persona3_title": "The Dividend Growth Collector",
        "persona3_body": "You already own NOBL for pure Aristocrat exposure but want more income now. KNG layers the options premium on top, letting you \"sell\" some future upside for current cash flow.",
        "scenario1_title": "Replacing Bond Income in a Low-Rate Environment",
        "scenario1_body": "Traditional bond funds yield 3-4%. KNG's ~7-8% monthly distribution from quality equity provides significantly more income with holdings you actually recognize — Colgate, Emerson, Dover.",
        "scenario2_title": "Portfolio Income Boost Without Junk Bonds",
        "scenario2_body": "To hit your 5% income target, you'd normally reach for high-yield bonds (junk). Instead, you add KNG — you get higher yields from dividend aristocrats plus option premium, without touching below-investment-grade debt.",
        "comp_ticker2": "NOBL", "comp_name2": "ProShares S&P 500 Dividend Aristocrats ETF",
        "comp_ticker3": "VIG", "comp_name3": "Vanguard Dividend Appreciation ETF",
        "comp_focus2": "Pure Dividend Aristocrats, no options", "comp_focus3": "Broad dividend growth, large-cap focus",
        "comp_strategy2": "Passive index, pure equity exposure", "comp_strategy3": "Passive, very low fee (0.06%)",
        "comp_pick2": "Lower fee, full upside capture from Aristocrats", "comp_pick3": "Lowest-cost dividend growth, maximum long-term compounding",
        "verdict": "KNG solves a real problem: how do you get 6-8% income from high-quality stocks without taking junk-bond risk? The answer is covered calls on dividend aristocrats. <strong>KNG is an excellent fit for income-first investors</strong> who prioritize monthly distributions and are comfortable giving up some equity upside. Just watch the fee and understand the tax treatment. <strong>For yield seekers who won't compromise on quality, KNG is royalty.</strong>",
    },
    "kngs": {
        "name": "Cboe Vest S&P 500 Dividend Aristocrats ETF",
        "ticker": "KNGS",
        "exchange": "AMEX",
        "quick_take": "KNGS is best for investors who want pure Dividend Aristocrat exposure (no options overlay) at a competitive cost. It is <em>not</em> a high-yield income ETF.",
        "summary": "<strong>KNGS (Cboe Vest S&P 500 Dividend Aristocrats ETF)</strong> is the straightforward, no-frills version of the Dividend Aristocrats strategy — companies that have raised their dividends for 50+ consecutive years (the Dividend Monarchs). No covered calls, no complexity, just the purest expression of long-term dividend discipline. If you want income <em>and</em> maximum long-term compounding with minimal strategy overhead, KNGS delivers.",
        "explained_intro": "What does 50 years of consecutive dividend increases look like in a portfolio? KNGS shows you.",
        "explained_body": "<p><strong>KNGS</strong> tracks a subset of the most committed dividend growers — companies that have increased dividends for <strong>50+ consecutive years</strong>. This elite cohort (\"Dividend Monarchs\") includes some of the most durable businesses ever built: think Kimberly-Clark, 3M, and Genuine Parts.</p><p>Here's why investors consider KNGS:\n<ul>\n<li><strong>Proven Durability:</strong> A 50-year dividend growth streak means the company survived stagflation, dot-com crash, 2008 GFC, COVID — and kept raising the payout.</li>\n<li><strong>Low Fee:</strong> At 0.25%, KNGS provides quality exposure at a fraction of what active dividend funds charge.</li>\n<li><strong>Dividend Growth Compounding:</strong> Rising dividends over time can outpace inflation and grow your income stream without you doing anything.</li>\n</ul>\n</p><p>Managed by <strong>Amplify ETFs</strong>, leveraging Cboe Vest methodology for index construction.</p>",
        "table_row": "<td>KNGS</td><td>Equity Dividend ETF</td><td>S&P 500 Dividend Aristocrats (Pure)</td><td>Quarterly</td><td>0.25%</td><td><a href=\"https://www.amplifyetfs.com/kngs\" target=\"_blank\" rel=\"noopener noreferrer\">Amplify ETFs</a></td>",
        "pro1": "<strong>50+ Year Dividend Streak:</strong> Holdings have raised dividends through every modern market crisis — the ultimate durability test.",
        "pro2": "<strong>Low Complexity:</strong> No options overlay — pure equity exposure with full upside participation.",
        "pro3": "<strong>Competitive Fee:</strong> 0.25% is reasonable for a curated quality index strategy.",
        "pro4": "<strong>Inflation-Fighting Income Growth:</strong> Rising dividends historically outpace inflation over long periods.",
        "con1": "<strong>Lower Current Yield:</strong> ~3% yield is solid but not spectacular compared to options-enhanced or high-yield funds.",
        "con2": "<strong>Limited Holdings:</strong> Fewer companies (Monarchs are a tiny club) means less diversification than broader funds.",
        "con3": "<strong>Sector Skew:</strong> Heavy Consumer Defensive and Industrials; limited Technology exposure.",
        "con4": "<strong>Small Fund:</strong> Lower AUM than NOBL or VIG means slightly less liquidity and potentially wider spreads.",
        "persona1_icon": "fas fa-hourglass-half",
        "persona1_title": "The Patient Compounder",
        "persona1_body": "You're building wealth over decades and want companies that will reliably grow your income every year. KNGS' Monarch holdings have proven they do exactly that — for 50+ years running.",
        "persona2_icon": "fas fa-university",
        "persona2_title": "The Quality-First Investor",
        "persona2_body": "You believe the best investments are boring, durable businesses. The 50-year dividend-growth requirement is one of the strictest quality filters in investing — KNGS distills it into one fund.",
        "persona3_icon": "fas fa-leaf",
        "persona3_title": "The Set-It-and-Forget-It Investor",
        "persona3_body": "You don't want to think about portfolio maintenance. KNGS holds the kind of companies that will still be raising dividends when you retire — just hold and collect.",
        "scenario1_title": "Building a Dividend Income Stream Over Time",
        "scenario1_body": "You start buying KNGS at 35. The yield is modest now, but as the underlying companies raise dividends 5-7% annually, your effective yield-on-cost grows substantially. By retirement, you're collecting meaningfully more income on the same shares.",
        "scenario2_title": "Anchoring a Conservative Allocation",
        "scenario2_body": "Your portfolio needs a stable equity anchor that won't collapse in bear markets. KNGS' Monarchs typically cut dividends last (or never) — they're the bedrock of a defensive equity allocation.",
        "comp_ticker2": "NOBL", "comp_name2": "ProShares S&P 500 Dividend Aristocrats ETF",
        "comp_ticker3": "VIG", "comp_name3": "Vanguard Dividend Appreciation ETF",
        "comp_focus2": "25+ year dividend growth streak (broader universe)", "comp_focus3": "10+ year dividend growth, very broad universe",
        "comp_strategy2": "Larger selection pool, more diversified", "comp_strategy3": "Widest selection, lowest fee (0.06%)",
        "comp_pick2": "More diversification at similar cost", "comp_pick3": "Maximum diversification and lowest cost",
        "verdict": "KNGS occupies a unique niche: the strictest quality filter in dividend investing (50-year streak), delivered at a fair price with no complexity. It won't win a yield contest against covered-call funds, but for <strong>long-term compounders who want bullet-proof dividend growers</strong>, KNGS is a compelling core holding. <strong>50 years of consecutive raises isn't luck — it's proof. KNGS packages that proof.</strong>",
    },
    "nobl": {
        "name": "ProShares S&P 500 Dividend Aristocrats ETF",
        "ticker": "NOBL",
        "exchange": "AMEX",
        "quick_take": "NOBL is best for investors seeking reliable dividend-growth exposure from S&P 500 blue chips. It is <em>not</em> a high-yield income fund.",
        "summary": "<strong>NOBL (ProShares S&P 500 Dividend Aristocrats ETF)</strong> is the flagship Dividend Aristocrats ETF — the go-to fund for owning the S&P 500 companies that have raised dividends for <strong>25+ consecutive years</strong>. Equal-weighted across ~65 qualifying companies, NOBL delivers consistent income growth, defensive characteristics, and blue-chip quality in a single, well-known package.",
        "explained_intro": "Want to own every S&P 500 company with a 25+ year dividend growth streak, all in one fund? NOBL has you covered.",
        "explained_body": "<p><strong>NOBL</strong> tracks the <strong>S&P 500 Dividend Aristocrats Index</strong>, which requires member companies to have increased dividends for at least <strong>25 consecutive years</strong> and be part of the S&P 500. The equal-weighting prevents mega-caps from dominating — every Aristocrat gets roughly the same piece of the pie.</p><p>Here's why investors consider NOBL:\n<ul>\n<li><strong>Quality Screen:</strong> 25-year consecutive increases is a powerful filter — it eliminates most dividend traps automatically.</li>\n<li><strong>Equal Weighting:</strong> No single company dominates; avoids the mega-cap concentration of market-cap-weighted funds.</li>\n<li><strong>Defensive Characteristics:</strong> Aristocrats historically drawdown less than the S&P 500 in bear markets.</li>\n</ul>\n</p><p>Managed by <strong>ProShares</strong>, one of the most recognized names in ETF product development.</p>",
        "table_row": "<td>NOBL</td><td>Equity Dividend ETF</td><td>S&P 500 Dividend Aristocrats (Equal-Weighted)</td><td>Quarterly</td><td>0.35%</td><td><a href=\"https://www.proshares.com/our-etfs/equity/nobl\" target=\"_blank\" rel=\"noopener noreferrer\">ProShares</a></td>",
        "pro1": "<strong>Proven Quality Filter:</strong> 25+ years of consecutive dividend growth is one of the most rigorous quality tests in public markets.",
        "pro2": "<strong>Equal Weighting:</strong> No mega-cap domination — each Aristocrat contributes equally, avoiding extreme concentration.",
        "pro3": "<strong>Bear Market Defense:</strong> Aristocrats historically fall less in downturns; dividend growers tend to be financially disciplined companies.",
        "pro4": "<strong>Established Track Record:</strong> NOBL has been the benchmark Aristocrats ETF since 2013 — battle-tested through multiple market cycles.",
        "con1": "<strong>Modest Yield (~2%):</strong> The income is reliable but not impressive — growth, not current yield, is the real appeal.",
        "con2": "<strong>Low Tech Exposure:</strong> Equal-weighting plus the dividend requirement limits technology stocks, which have driven recent market returns.",
        "con3": "<strong>Higher Fee vs. VIG:</strong> 0.35% is reasonable but Vanguard's VIG (0.06%) provides a similar strategy cheaper.",
        "con4": "<strong>May Lag in Growth Rallies:</strong> When mega-cap tech dominates (like 2020-2023), equal-weighted dividend stocks can significantly underperform.",
        "persona1_icon": "fas fa-award",
        "persona1_title": "The Dividend Growth Investor",
        "persona1_body": "You believe in buying quality companies with growing dividends and holding them forever. NOBL is literally an index of the best dividend growers in America's largest companies.",
        "persona2_icon": "fas fa-umbrella",
        "persona2_title": "The Bear Market Prepper",
        "persona2_body": "You're worried about a correction and want equity exposure that historically falls less than the broad market. Dividend Aristocrats' financial discipline tends to limit downside in panics.",
        "persona3_icon": "fas fa-building",
        "persona3_title": "The Institutional-Grade Core Holder",
        "persona3_body": "You want a core equity holding that's transparent, rules-based, easy to explain, and backed by decades of academic support for dividend-growth investing. NOBL checks every box.",
        "scenario1_title": "Core Equity Holding in a Conservative Portfolio",
        "scenario1_body": "You're building a portfolio for a parent or retiree. NOBL provides S&P 500 quality without the mega-cap tech concentration of SPY. It's grown dividends through every recession since the late 1980s.",
        "scenario2_title": "Tactical Rotation Out of Growth",
        "scenario2_body": "You're rotating from growth-heavy positions (QQQ, VGT) toward value and income as the rate environment shifts. NOBL is the natural landing spot — quality, diversified, income-growing.",
        "comp_ticker2": "VIG", "comp_name2": "Vanguard Dividend Appreciation ETF",
        "comp_ticker3": "KNG", "comp_name3": "FT Cboe Vest S&P 500 Dividend Aristocrats Target Income ETF",
        "comp_focus2": "10+ year dividend growth, much broader universe", "comp_focus3": "Same Aristocrats universe + covered-call income boost",
        "comp_strategy2": "Passive, very low fee (0.06%), 300+ holdings", "comp_strategy3": "Options overlay generates ~7-8% yield",
        "comp_pick2": "If you want maximum diversification at minimum cost", "comp_pick3": "If you need higher current income from the same holdings",
        "verdict": "NOBL is the <strong>gold standard for dividend-growth investing</strong> in a single, transparent package. The 25-year streak requirement is a powerful quality filter, and equal weighting ensures you're not just buying large-cap tech in disguise. It won't outperform SPY in every bull market, but over full cycles, the quality and income-growth combination is compelling. <strong>For dividend-growth believers, NOBL is the benchmark you measure everything else against.</strong>",
    },
    "pbp": {
        "name": "Invesco S&P 500 BuyWrite ETF",
        "ticker": "PBP",
        "exchange": "AMEX",
        "quick_take": "PBP is best for investors seeking to reduce portfolio volatility and generate income from their S&P 500 exposure. It is <em>not</em> a growth ETF.",
        "summary": "<strong>PBP (Invesco S&P 500 BuyWrite ETF)</strong> implements the classic \"covered call\" strategy on the S&P 500 — you own the index stocks and sell call options against them every month. The option premium becomes income. In exchange, your upside in roaring bull markets is capped. The result: lower volatility, higher income, and better performance in flat or declining markets compared to a plain S&P 500 fund.",
        "explained_intro": "What if your S&P 500 exposure paid you extra income every month, even when the market went nowhere?",
        "explained_body": "<p><strong>PBP</strong> holds an S&P 500 portfolio and systematically sells monthly <strong>at-the-money call options</strong> against it. This is the \"BuyWrite\" (buy stock, write calls) strategy, one of the oldest income-enhancement techniques in finance.</p><p>Here's why investors consider PBP:\n<ul>\n<li><strong>Option Premium Income:</strong> Monthly call premiums add consistent income regardless of whether the market goes up, down, or sideways.</li>\n<li><strong>Volatility Reduction:</strong> The premium collected creates a buffer against small drawdowns — PBP typically falls less than SPY in moderate declines.</li>\n<li><strong>S&P 500 Quality:</strong> You still own the largest, most financially sound U.S. companies as the underlying portfolio.</li>\n</ul>\n</p><p>Managed by <strong>Invesco</strong>, a major global investment management firm.</p>",
        "table_row": "<td>PBP</td><td>Equity Dividend ETF</td><td>S&P 500 BuyWrite (Covered Call)</td><td>Monthly</td><td>0.49%</td><td><a href=\"https://www.invesco.com/us/financial-products/etfs/product-detail?audienceType=Investor&ticker=PBP\" target=\"_blank\" rel=\"noopener noreferrer\">Invesco</a></td>",
        "pro1": "<strong>Monthly Income Generation:</strong> Option premiums deposited monthly, regardless of market direction — income even in flat markets.",
        "pro2": "<strong>Lower Volatility:</strong> Premium buffer reduces the sting of moderate drawdowns compared to unhedged S&P 500 exposure.",
        "pro3": "<strong>S&P 500 Quality Base:</strong> Underlying holdings are the same blue-chip companies in SPY — quality is not sacrificed.",
        "pro4": "<strong>Defensively Positioned:</strong> Tends to outperform SPY in flat, sideways, or mildly declining markets — the majority of market environments.",
        "con1": "<strong>Capped Upside:</strong> When the S&P 500 surges (e.g., +20% years), PBP significantly lags because calls get exercised at the strike.",
        "con2": "<strong>Underperforms in Strong Bull Markets:</strong> In 2019, 2020-rebound, 2023 — PBP lagged SPY materially due to call caps.",
        "con3": "<strong>Fee vs. SPY:</strong> 0.49% vs. SPY's 0.095% — you pay substantially more for the options strategy.",
        "con4": "<strong>Tax Complexity:</strong> Option income distributions may be treated as ordinary income, not the favorable qualified dividend rate.",
        "persona1_icon": "fas fa-tachometer-alt",
        "persona1_title": "The Low-Volatility Seeker",
        "persona1_body": "You want S&P 500 exposure but lose sleep when markets swing 3-5% in a day. PBP's premium buffer smooths the ride significantly, making it easier to stay invested through volatility.",
        "persona2_icon": "fas fa-coins",
        "persona2_title": "The Income Optimizer",
        "persona2_body": "You're not satisfied with SPY's ~1.5% yield. PBP's monthly premiums can push effective yield to 5%+, making your S&P 500 allocation work much harder on the income front.",
        "persona3_icon": "fas fa-chart-bar",
        "persona3_title": "The Sideways Market Navigator",
        "persona3_body": "You believe the market is entering a choppy, range-bound period (as it often does after big runs). PBP collects premium in exactly those conditions — you get paid to wait.",
        "scenario1_title": "Enhancing Income in a Market Plateau",
        "scenario1_body": "After a big S&P 500 run, you believe the market needs time to consolidate. You shift from SPY to PBP — you keep your market exposure but collect monthly premiums while the market chops sideways for 12 months.",
        "scenario2_title": "Replacing Bond Income With Equity Income",
        "scenario2_body": "Bonds yield 4%. You'd rather get income from equities to maintain long-term growth potential. PBP gives you S&P 500 quality with a monthly income stream that competes with bond yields in many rate environments.",
        "comp_ticker2": "XYLD", "comp_name2": "Global X S&P 500 Covered Call ETF",
        "comp_ticker3": "JEPI", "comp_name3": "JPMorgan Equity Premium Income ETF",
        "comp_focus2": "S&P 500 covered call, higher yield target", "comp_focus3": "Lower-volatility S&P 500 stocks + ELN income",
        "comp_strategy2": "Writes calls on full SPX index; higher income cap", "comp_strategy3": "Actively selects defensive stocks + equity-linked notes",
        "comp_pick2": "If you want maximum income yield from covered calls", "comp_pick3": "If you want active management with slightly different risk profile",
        "verdict": "PBP is the <strong>original BuyWrite ETF</strong> and still a solid choice for income-seeking S&P 500 investors who are willing to give up some bull-market upside. In choppy or declining markets, it consistently outperforms. In raging bull markets, it lags. Know your market outlook before choosing PBP. <strong>If the bull is tired and you need income, PBP is your workhorse.</strong>",
    },
    "pey": {
        "name": "Invesco High Yield Equity Dividend Achievers ETF",
        "ticker": "PEY",
        "exchange": "AMEX",
        "quick_take": "PEY is best for income seekers who want above-average dividend yield from smaller dividend achievers. It is <em>not</em> a growth or safety-first fund.",
        "summary": "<strong>PEY (Invesco High Yield Equity Dividend Achievers ETF)</strong> screens for U.S. stocks with the highest dividend yields among those with 10+ consecutive years of dividend increases — the \"Dividend Achievers.\" You get a concentrated, high-yield income fund built from dividend-growth companies, skewing toward utilities, financials, and other traditionally high-yielding sectors.",
        "explained_intro": "Want higher dividend income from companies that have been growing their payouts for a decade? PEY finds them.",
        "explained_body": "<p><strong>PEY</strong> tracks the <strong>NASDAQ US Dividend Achievers 50 Index</strong> — the 50 highest-yielding stocks from the universe of companies with 10+ consecutive years of dividend growth. Yield-weighting means the highest payers get the largest allocations.</p><p>Here's why investors consider PEY:\n<ul>\n<li><strong>High Current Yield:</strong> By selecting the highest-yielding Achievers, PEY delivers meaningfully more income than broad dividend ETFs.</li>\n<li><strong>Dividend Growth History:</strong> The 10-year requirement filters out dividend traps — these companies have proven they can maintain and grow payouts.</li>\n<li><strong>Sector Diversification:</strong> While yield-heavy, PEY spans utilities, financials, energy, and consumer staples for reasonable diversification.</li>\n</ul>\n</p><p>Managed by <strong>Invesco</strong>, one of the largest ETF providers globally.</p>",
        "table_row": "<td>PEY</td><td>Equity Dividend ETF</td><td>High-Yield Dividend Achievers</td><td>Monthly</td><td>0.52%</td><td><a href=\"https://www.invesco.com/us/financial-products/etfs/product-detail?audienceType=Investor&ticker=PEY\" target=\"_blank\" rel=\"noopener noreferrer\">Invesco</a></td>",
        "pro1": "<strong>Above-Average Yield:</strong> Typically delivers 4-5%+ yield, well above VYM, SCHD, or plain dividend-growth ETFs.",
        "pro2": "<strong>Monthly Distributions:</strong> Income paid monthly, which is ideal for retirees managing regular expenses.",
        "pro3": "<strong>Dividend Growth Discipline:</strong> 10-year consecutive increase requirement weeds out dividend traps before they appear in the fund.",
        "pro4": "<strong>Proven Achievers:</strong> Holdings have a demonstrated ability to grow dividends through economic cycles — not just yield chasers.",
        "con1": "<strong>Value/Rate Sensitivity:</strong> High-yield, value-oriented sectors (utilities, financials) are very sensitive to interest rate changes.",
        "con2": "<strong>Limited Growth Exposure:</strong> The yield focus systematically excludes high-growth companies that pay modest dividends.",
        "con3": "<strong>Concentration Risk:</strong> Only 50 holdings; sector tilts to utilities and financials can hurt in certain market environments.",
        "con4": "<strong>Moderate Fee:</strong> 0.52% is reasonable but adds up over time versus lower-cost dividend alternatives.",
        "persona1_icon": "fas fa-money-bill-wave",
        "persona1_title": "The Retiree Living on Dividends",
        "persona1_body": "You need monthly income to cover expenses. PEY's above-average yield paid monthly matches your cash-flow needs, and the dividend growth history means your purchasing power grows over time.",
        "persona2_icon": "fas fa-percentage",
        "persona2_title": "The Yield Maximizer (with Quality)",
        "persona2_body": "You want the highest yield possible but won't take junk bonds or dividend traps. PEY's Achievers screen gives you higher income than VYM or SCHD with a built-in quality filter.",
        "persona3_icon": "fas fa-piggy-bank",
        "persona3_title": "The Conservative Income Builder",
        "persona3_body": "You're in the accumulation phase but want income reinvested at a higher yield than typical dividend ETFs. PEY's DRIP compound effect at 4-5% yield accelerates income snowballing.",
        "scenario1_title": "Building a Retirement Income Layer",
        "scenario1_body": "You're 3-5 years from retirement and want to start building an income stream. You allocate part of your equity bucket to PEY — the monthly distributions start flowing, and you reinvest until you actually need the cash.",
        "scenario2_title": "Offsetting a Low-Yield Bond Portfolio",
        "scenario2_body": "Your bond allocation only yields 3%. You replace a slice of it with PEY to improve overall portfolio income. The dividend-growth history provides more stability than you'd expect from a high-yield designation.",
        "comp_ticker2": "VYM", "comp_name2": "Vanguard High Dividend Yield ETF",
        "comp_ticker3": "SCHD", "comp_name3": "Schwab U.S. Dividend Equity ETF",
        "comp_focus2": "Broad high-yield, large-cap, very low fee (0.06%)", "comp_focus3": "Quality dividend growers, quarterly, very low fee (0.06%)",
        "comp_strategy2": "400+ holdings, market-cap weighted, lower yield", "comp_strategy3": "Quality screen + dividend growth, slightly lower yield than PEY",
        "comp_pick2": "Lower cost, more diversified, slightly lower yield", "comp_pick3": "Better quality screen at much lower cost",
        "verdict": "PEY fills a specific niche: income-seekers who want more than VYM or SCHD deliver but are unwilling to abandon dividend-growth discipline entirely. The monthly payments and above-average yield make it genuinely useful for retirees or income-focused accumulators. The trade-off is rate sensitivity and limited growth exposure. <strong>If you need income now and want companies that have been growing their dividends for a decade, PEY delivers.</strong>",
    },
    "qqew": {
        "name": "First Trust NASDAQ-100 Equal Weighted Index Fund",
        "ticker": "QQEW",
        "exchange": "NASDAQ",
        "quick_take": "QQEW is best for investors who want NASDAQ-100 exposure without mega-cap concentration risk. It is <em>not</em> a high-yield income fund.",
        "summary": "<strong>QQEW (First Trust NASDAQ-100 Equal Weighted Index Fund)</strong> owns all 100 companies in the NASDAQ-100 — but weights them equally instead of by market cap. This means Apple and Microsoft get the same allocation as Illumina or Mondelez. The result: better diversification, more mid-cap exposure within the index, and a very different return profile than QQQ in years when mega-caps dominate or struggle.",
        "explained_intro": "What if the NASDAQ-100 treated Apple and a $10B biotech as equals? QQEW finds out.",
        "explained_body": "<p><strong>QQEW</strong> holds the same 100 non-financial companies as the <strong>NASDAQ-100 Index</strong> but rebalances them to <strong>equal weights</strong> quarterly. Each holding starts at ~1% of the portfolio, giving smaller NASDAQ-100 members a far greater influence than in QQQ.</p><p>Here's why investors consider QQEW:\n<ul>\n<li><strong>Diversification Within NASDAQ-100:</strong> Equal weighting eliminates the top-heavy problem — in QQQ, the top 5 stocks often represent 40%+ of the index.</li>\n<li><strong>Mid-Cap Tilt:</strong> Equal weighting effectively tilts toward smaller NASDAQ-100 companies, which can outperform when mega-caps are under pressure.</li>\n<li><strong>Same Quality Universe:</strong> Still the NASDAQ-100's rigorous liquidity and revenue requirements — quality isn't sacrificed.</li>\n</ul>\n</p><p>Managed by <strong>First Trust Advisors</strong>, a major ETF provider known for smart-beta and equal-weight strategies.</p>",
        "table_row": "<td>QQEW</td><td>Equity ETF</td><td>NASDAQ-100 Equal Weighted</td><td>Quarterly</td><td>0.58%</td><td><a href=\"https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=QQEW\" target=\"_blank\" rel=\"noopener noreferrer\">First Trust Advisors</a></td>",
        "pro1": "<strong>Reduced Mega-Cap Concentration:</strong> Apple and Microsoft don't dominate; you get genuine diversification across all 100 NASDAQ-100 names.",
        "pro2": "<strong>Mid-Cap Alpha Potential:</strong> Equal weighting tilts toward smaller members that can outperform when market leadership broadens.",
        "pro3": "<strong>Same Quality Bar as QQQ:</strong> NASDAQ-100 membership requires size, liquidity, and revenue thresholds — quality is built in.",
        "pro4": "<strong>Built-In Rebalancing:</strong> Quarterly equal-weight rebalancing forces a systematic \"sell high, buy low\" discipline.",
        "con1": "<strong>Underperforms in Mega-Cap Bull Markets:</strong> When Apple, Microsoft, and Nvidia dominate (2020-2023), QQEW significantly lags QQQ.",
        "con2": "<strong>Higher Fee:</strong> 0.58% vs. QQQ's 0.20% — you pay a meaningful premium for equal weighting.",
        "con3": "<strong>Lower Liquidity vs. QQQ:</strong> QQEW's AUM is a fraction of QQQ's; spreads can be wider.",
        "con4": "<strong>Rebalancing Drag:</strong> Quarterly rebalancing generates turnover and potential tax drag compared to buy-and-hold cap-weighted.",
        "persona1_icon": "fas fa-balance-scale",
        "persona1_title": "The Concentration-Averse Tech Investor",
        "persona1_body": "You want NASDAQ-100 exposure but feel uncomfortable with 40%+ in 5 stocks. QQEW lets you own the same universe with genuine diversification across all 100 names.",
        "persona2_icon": "fas fa-expand-arrows-alt",
        "persona2_title": "The Market Broadening Beter",
        "persona2_body": "You believe the era of mega-cap dominance is ending and market leadership will broaden. Equal weighting is precisely positioned to capture that — when the \"other 95\" outperform, QQEW shines.",
        "persona3_icon": "fas fa-layer-group",
        "persona3_title": "The QQQ Complement Seeker",
        "persona3_body": "You already own QQQ for mega-cap tech. Adding QQEW lets you tilt toward the smaller NASDAQ-100 members — effectively expanding your exposure within the same quality universe.",
        "scenario1_title": "Positioning for Market Broadening",
        "scenario1_body": "After years of mega-cap dominance, analysts predict leadership rotation to mid-caps and value. You shift from QQQ to QQEW (or blend both) to benefit from NASDAQ-100 breadth expansion without abandoning the index.",
        "scenario2_title": "Reducing Individual Stock Concentration Risk",
        "scenario2_body": "Your 401k already has heavy Apple and Microsoft exposure through your S&P 500 index fund. Adding QQEW instead of QQQ gives you NASDAQ-100 upside without doubling down on the mega-cap concentrations you already have.",
        "comp_ticker2": "QQQ", "comp_name2": "Invesco QQQ Trust",
        "comp_ticker3": "QQQM", "comp_name3": "Invesco NASDAQ 100 ETF",
        "comp_focus2": "NASDAQ-100, cap-weighted (mega-cap heavy)", "comp_focus3": "Same as QQQ, lower fee, for long-term holders",
        "comp_strategy2": "Passive cap-weight, dominant in mega-cap tech", "comp_strategy3": "Passive cap-weight, 0.15% fee vs QQQ's 0.20%",
        "comp_pick2": "If you believe mega-caps continue to dominate", "comp_pick3": "If you want standard NASDAQ-100 at lowest cost",
        "verdict": "QQEW is the <strong>antidote to mega-cap concentration</strong> within the NASDAQ-100. It consistently underperforms QQQ when Apple, Microsoft, and Nvidia lead, and outperforms when leadership broadens. The higher fee is the real hurdle — you're paying for equal weighting, and the market has to cooperate for that premium to pay off. <strong>For investors who believe the next decade belongs to the \"other 95\" in NASDAQ, QQEW is the vehicle.</strong>",
    },
    "qqqm": {
        "name": "Invesco NASDAQ 100 ETF",
        "ticker": "QQQM",
        "exchange": "NASDAQ",
        "quick_take": "QQQM is best for long-term buy-and-hold investors who want NASDAQ-100 exposure at the lowest possible cost. It is essentially QQQ, slightly cheaper.",
        "summary": "<strong>QQQM (Invesco NASDAQ 100 ETF)</strong> is Invesco's lower-cost, buy-and-hold-optimized version of the legendary QQQ. Same index, same 100 companies, lower expense ratio. The only meaningful difference: QQQM is designed for retail long-term investors, while QQQ is built for institutional traders who need extreme liquidity. If you're not an institutional trader, QQQM is simply the smarter way to own the NASDAQ-100.",
        "explained_intro": "Same NASDAQ-100, lower fee. QQQM is QQQ's younger, more cost-efficient sibling for long-term investors.",
        "explained_body": "<p><strong>QQQM</strong> tracks the <strong>NASDAQ-100 Index</strong> — 100 of the largest non-financial companies listed on the NASDAQ, heavily weighted toward technology (Apple, Microsoft, NVIDIA, Amazon, Meta). It is <strong>identical in holdings and weighting</strong> to QQQ but carries a lower expense ratio (0.15% vs. 0.20%).</p><p>Here's why investors consider QQQM:\n<ul>\n<li><strong>Cost Efficiency:</strong> Over decades of holding, the fee savings compound meaningfully — 0.05% per year adds up to thousands of dollars on a large position.</li>\n<li><strong>NASDAQ-100 Performance:</strong> The index has been one of the best-performing over 15+ year periods, driven by Big Tech's dominance.</li>\n<li><strong>Simpler Than QQQ:</strong> QQQM has a smaller share price (more accessible) and is optimized for retail investor tax efficiency.</li>\n</ul>\n</p><p>Managed by <strong>Invesco</strong>, which launched QQQM specifically to serve the growing retail investor demand for low-cost, long-term NASDAQ-100 exposure.</p>",
        "table_row": "<td>QQQM</td><td>Equity ETF</td><td>NASDAQ-100 Index (Cap-Weighted)</td><td>Quarterly</td><td>0.15%</td><td><a href=\"https://www.invesco.com/us/financial-products/etfs/product-detail?audienceType=Investor&ticker=QQQM\" target=\"_blank\" rel=\"noopener noreferrer\">Invesco</a></td>",
        "pro1": "<strong>Lower Cost Than QQQ:</strong> 0.15% vs. 0.20% — a small difference that compounds significantly over decades of holding.",
        "pro2": "<strong>Full NASDAQ-100 Exposure:</strong> Same Apple, Microsoft, NVIDIA, Amazon, Meta, Alphabet concentration that has driven massive long-term returns.",
        "pro3": "<strong>Long-Term Optimized:</strong> Designed for buy-and-hold retail investors with better tax efficiency features than QQQ.",
        "pro4": "<strong>Lower Share Price:</strong> Easier to dollar-cost average and invest in smaller amounts compared to QQQ's higher per-share price.",
        "con1": "<strong>Mega-Cap Concentration:</strong> Top 5-7 stocks represent 40-50% of the fund — extraordinary concentration in a handful of companies.",
        "con2": "<strong>Less Liquid Than QQQ:</strong> For large institutional trades, QQQ's massive daily volume is superior; QQQM's spreads can be wider.",
        "con3": "<strong>Limited Dividend Income:</strong> Yield is around 0.6-0.8% — essentially zero income; total return is almost entirely capital appreciation.",
        "con4": "<strong>Tech Sector Risk:</strong> When tech sells off (2022: -33%), QQQM takes the full hit; no defensive diversification.",
        "persona1_icon": "fas fa-rocket",
        "persona1_title": "The Long-Term Growth Investor",
        "persona1_body": "You believe Big Tech will continue to dominate for the next decade. QQQM gives you the most cost-efficient, long-term access to Apple, NVIDIA, Microsoft, and Amazon in one purchase.",
        "persona2_icon": "fas fa-piggy-bank",
        "persona2_title": "The DCA Accumulator",
        "persona2_body": "You invest a fixed amount every month. QQQM's lower share price (vs QQQ) makes monthly DCA more precise, and the lower expense ratio means more of your money compounds rather than paying fees.",
        "persona3_icon": "fas fa-trophy",
        "persona3_title": "The QQQ Migrator",
        "persona3_body": "You already own QQQ in a taxable account and don't want to trigger a taxable event. For your retirement or new accounts, you buy QQQM going forward — same exposure, better economics for buy-and-hold.",
        "scenario1_title": "IRA or 401k NASDAQ-100 Allocation",
        "scenario1_body": "In your retirement account, you want maximum NASDAQ-100 exposure for long-term growth. QQQM's 0.15% fee saves you 0.05% vs. QQQ annually — in a $200k position over 20 years, that's thousands of dollars in additional compound growth.",
        "scenario2_title": "Core Growth Position in Brokerage",
        "scenario2_body": "Your core strategy is simple: own the NASDAQ-100 and hold for 20+ years. QQQM executes that strategy at the lowest cost Invesco offers, with the exact same 100-company portfolio that has delivered exceptional long-term returns.",
        "comp_ticker2": "QQQ", "comp_name2": "Invesco QQQ Trust",
        "comp_ticker3": "QQEW", "comp_name3": "First Trust NASDAQ-100 Equal Weighted Index Fund",
        "comp_focus2": "Identical index, higher fee (0.20%), ultra-liquid for institutions", "comp_focus3": "Same 100 companies, equal-weighted (less mega-cap concentration)",
        "comp_strategy2": "Cap-weighted, institutional-grade liquidity", "comp_strategy3": "Equal-weight, rebalanced quarterly",
        "comp_pick2": "If you're an institutional trader requiring maximum liquidity", "comp_pick3": "If you want NASDAQ-100 breadth without mega-cap dominance",
        "verdict": "QQQM is <strong>simply the better version of QQQ for long-term retail investors</strong>. Identical exposure, lower cost, optimized for buy-and-hold. The case for choosing QQQ over QQQM is essentially \"I need institutional-grade liquidity\" — most retail investors don't. <strong>If you believe in the NASDAQ-100 and plan to hold for years, QQQM is the rational choice. Just buy it and compound.</strong>",
    },
    "qqqn": {
        "name": "VictoryShares NASDAQ Next 50 ETF",
        "ticker": "QQQN",
        "exchange": "NASDAQ",
        "quick_take": "QQQN is best for growth investors who want exposure to the 50 companies most likely to join the NASDAQ-100 next. It is <em>not</em> a conservative or income fund.",
        "summary": "<strong>QQQN (VictoryShares NASDAQ Next 50 ETF)</strong> owns the 51st-100th largest non-financial NASDAQ companies — the companies right on the doorstep of the NASDAQ-100. Think of it as a \"farm team\" for QQQ: today's QQQN holding could become tomorrow's NASDAQ-100 member. This is where emerging technology, biotechnology, and consumer disruptors live before hitting the big league.",
        "explained_intro": "What companies will join the NASDAQ-100 next? QQQN owns them now, before the promotion.",
        "explained_body": "<p><strong>QQQN</strong> tracks the <strong>NASDAQ Next 50 Index</strong> — the 50 companies ranked 51st to 100th by market capitalization among NASDAQ-listed non-financial firms. These are the next-tier companies, many of which will be promoted to the NASDAQ-100 as they grow.</p><p>Here's why investors consider QQQN:\n<ul>\n<li><strong>Pre-Promotion Exposure:</strong> When a QQQN holding gets promoted to the NASDAQ-100, QQQ must buy it — creating potential price appreciation before inclusion.</li>\n<li><strong>Mid-Cap Growth:</strong> These companies are smaller and earlier-stage than NASDAQ-100 giants, offering higher growth potential (with higher risk).</li>\n<li><strong>NASDAQ Quality:</strong> Still subject to NASDAQ's listing requirements — meaningful revenue and liquidity minimums filter out the smallest speculative names.</li>\n</ul>\n</p><p>Managed by <strong>VictoryShares</strong>, a Cincinnati-based ETF provider focused on smart-beta and factor strategies.</p>",
        "table_row": "<td>QQQN</td><td>Equity ETF</td><td>NASDAQ Next 50 (Pre-QQQ)</td><td>Quarterly</td><td>0.15%</td><td><a href=\"https://www.victoryshares.com/etfs/qqqn\" target=\"_blank\" rel=\"noopener noreferrer\">VictoryShares</a></td>",
        "pro1": "<strong>Pre-Promotion Alpha:</strong> Owning future NASDAQ-100 members before QQQ is forced to buy them can generate meaningful price appreciation.",
        "pro2": "<strong>Mid-Cap Growth Sweet Spot:</strong> These companies are large enough to be proven but small enough to still have significant growth runways.",
        "pro3": "<strong>NASDAQ Quality Filter:</strong> Revenue and liquidity requirements mean you're not holding micro-cap speculative companies.",
        "pro4": "<strong>Complementary to QQQ:</strong> QQQN and QQQ together cover the full top-100 NASDAQ non-financial universe comprehensively.",
        "con1": "<strong>Higher Volatility:</strong> Mid-cap tech and biotech swing harder than the mega-caps in QQQ — QQQN can drop significantly in risk-off environments.",
        "con2": "<strong>Demotion Risk:</strong> Companies can also be removed from the NASDAQ-100 into QQQN's universe — these are already declining.",
        "con3": "<strong>Low Dividend Yield:</strong> Growth companies at this stage rarely pay significant dividends — income is minimal.",
        "con4": "<strong>Smaller AUM:</strong> Less liquidity than QQQ/QQQM; smaller fund size means slightly wider spreads and less institutional validation.",
        "persona1_icon": "fas fa-binoculars",
        "persona1_title": "The Early Mover",
        "persona1_body": "You want to own the next Apple, the next NVIDIA — before they're household names. QQQN holds the companies that are growing toward NASDAQ-100 inclusion, offering exposure to emerging leaders early.",
        "persona2_icon": "fas fa-chess",
        "persona2_title": "The QQQ Complement Strategist",
        "persona2_body": "You own QQQ for mega-cap tech. You add QQQN to fill the 51-100 tier — together, they give you comprehensive NASDAQ coverage beyond just the top 10 or 20 names.",
        "persona3_icon": "fas fa-running",
        "persona3_title": "The High-Conviction Growth Investor",
        "persona3_body": "You believe technology and innovation will continue to create enormous value over the next 10-20 years. QQQN lets you concentrate in the next wave of winners without hand-picking individual stocks.",
        "scenario1_title": "Satellite Growth Allocation",
        "scenario1_body": "Your core is SPY and QQQ. You allocate 5-10% to QQQN as a \"growth satellite\" — you're betting on the next generation of NASDAQ stars while your core holdings provide stability.",
        "scenario2_title": "Pairing QQQN + QQQ for Full Coverage",
        "scenario2_body": "You believe in the NASDAQ universe broadly and want more than just the top 100. Pairing QQQ (companies 1-100) with QQQN (companies 51-100 from Next 50) gives you broad exposure to the full NASDAQ growth ecosystem.",
        "comp_ticker2": "QQQ", "comp_name2": "Invesco QQQ Trust",
        "comp_ticker3": "QQQM", "comp_name3": "Invesco NASDAQ 100 ETF",
        "comp_focus2": "NASDAQ-100 (top 100), mega-cap dominant", "comp_focus3": "Same as QQQ, lower fee, buy-and-hold optimized",
        "comp_strategy2": "Cap-weighted, established mega-caps dominate", "comp_strategy3": "Cap-weighted, slightly lower fee than QQQ",
        "comp_pick2": "If you want established NASDAQ leaders (lower risk)", "comp_pick3": "If you want NASDAQ-100 at lowest cost for long-term hold",
        "verdict": "QQQN is a <strong>specialized growth tool</strong> — best as a satellite allocation, not a core holding. Its \"farm team\" positioning creates genuine alpha opportunities when companies get promoted to the NASDAQ-100. The higher volatility and lower liquidity are real trade-offs. <strong>For aggressive growth investors who want to own tomorrow's QQQ leaders today, QQQN offers a compelling edge.</strong>",
    },
}


def build_new_sections(data):
    ticker = data["ticker"]
    name = data["name"]
    exchange = data["exchange"]

    sections = f"""
                <section id="bottom-line" class="section-grey">
                    <div class="summary-box">
                        <h2>The Bottom Line Up Front</h2>
                        <p><strong>Quick take:</strong> {data["quick_take"]}</p>
                        <p>{data["summary"]}</p>
                    </div>
                </section>

                <section id="overview" class="section-white">
                    <h2>{ticker} Explained: What It Is and Why It Matters</h2>
                    <p>{data["explained_intro"]}</p>
                    {data["explained_body"]}
                    <div class="table-container text-center mb-4">
                        <table class="etf-table">
                            <thead>
                                <tr>
                                    <th>Ticker Symbol</th>
                                    <th>Asset Class</th>
                                    <th>Strategy</th>
                                    <th>Payment Frequency</th>
                                    <th>Expense Ratio</th>
                                    <th>Sponsor</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    {data["table_row"]}
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <section id="pros-cons" class="section-grey">
                    <h2>{ticker}: The Good, The Bad, and The Reality</h2>
                    <p>Every investment has its strengths and weaknesses. Here's what makes {ticker} stand out for some investors, and a miss for others.</p>
                    <div class="table-container">
                        <table class="pros-cons-table">
                            <thead>
                                <tr>
                                    <th class="w-50">Pros <i class="fas fa-check-circle green-check"></i></th>
                                    <th class="w-50">Cons <i class="fas fa-times-circle red-x"></i></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>{data["pro1"]}</td>
                                    <td>{data["con1"]}</td>
                                </tr>
                                <tr>
                                    <td>{data["pro2"]}</td>
                                    <td>{data["con2"]}</td>
                                </tr>
                                <tr>
                                    <td>{data["pro3"]}</td>
                                    <td>{data["con3"]}</td>
                                </tr>
                                <tr>
                                    <td>{data["pro4"]}</td>
                                    <td>{data["con4"]}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <section id="who-should-buy" class="section-white">
                    <h2>Who Should Consider {ticker}?</h2>
                    <p>Is {ticker} the right fit for your money? It depends on your goals and risk tolerance. Here are three common investor profiles where {ticker} shines:</p>

                    <div class="persona-box">
                        <h3><i class="{data["persona1_icon"]}"></i> {data["persona1_title"]}</h3>
                        <p>{data["persona1_body"]}</p>
                    </div>

                    <div class="persona-box">
                        <h3><i class="{data["persona2_icon"]}"></i> {data["persona2_title"]}</h3>
                        <p>{data["persona2_body"]}</p>
                    </div>

                    <div class="persona-box">
                        <h3><i class="{data["persona3_icon"]}"></i> {data["persona3_title"]}</h3>
                        <p>{data["persona3_body"]}</p>
                    </div>
                </section>

                <section id="scenarios" class="section-grey">
                    <h2>{ticker} in Action: Real-World Scenarios</h2>
                    <p>Let's look at how everyday investors actually use {ticker} in their financial lives:</p>
                    <ul>
                        <li>
                            <p><strong>{data["scenario1_title"]}:</strong> {data["scenario1_body"]}</p>
                        </li>
                        <li>
                            <p><strong>{data["scenario2_title"]}:</strong> {data["scenario2_body"]}</p>
                        </li>
                    </ul>
                </section>

                <section id="comparison" class="section-white">
                    <h2>{ticker} vs. The Competition: A Quick Look</h2>
                    <p>While {ticker} is a popular choice, it's not the only option. Here's a simplified comparison with two close competitors:</p>
                    <div class="table-container text-center mb-4">
                        <table class="etf-comparison-table">
                            <thead>
                                <tr>
                                    <th>Feature</th>
                                    <th>{ticker}</th>
                                    <th>{data["comp_ticker2"]} ({data["comp_name2"]})</th>
                                    <th>{data["comp_ticker3"]} ({data["comp_name3"]})</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Investment Focus</strong></td>
                                    <td>{name}</td>
                                    <td>{data["comp_focus2"]}</td>
                                    <td>{data["comp_focus3"]}</td>
                                </tr>
                                <tr>
                                    <td><strong>Strategy</strong></td>
                                    <td>See table above</td>
                                    <td>{data["comp_strategy2"]}</td>
                                    <td>{data["comp_strategy3"]}</td>
                                </tr>
                                <tr>
                                    <td><strong>Why You Might Pick It</strong></td>
                                    <td>See verdict below</td>
                                    <td>{data["comp_pick2"]}</td>
                                    <td>{data["comp_pick3"]}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <section id="final-verdict" class="section-grey">
                    <div class="final-verdict-box">
                        <h2>The Richiest.com Final Verdict: Is {ticker} Right For You?</h2>
                        <p>{data["verdict"]}</p>
                    </div>
                </section>
"""
    return sections


def retouch_file(ticker, data):
    filepath = f"{BASE}/{ticker}.html"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the author box closing pattern and the next section start
    # Pattern: </div>\n                        </div>\n                    </div>\n                </section>\n                <section id="position">
    # We insert new sections AFTER the author section closing and BEFORE the position section

    # Look for the end of the author section (first unnamed <section>) and before <section id="position">
    # The author section ends with the closing </section> tag before <section id="position">
    insert_marker = '</section>\n                <section id="position">'
    
    if insert_marker not in content:
        # Try alternative whitespace
        insert_marker = '</section>\n            <section id="position">'
    
    if insert_marker not in content:
        print(f"WARNING: Could not find insert marker in {ticker}.html")
        return False

    new_sections = build_new_sections(data)
    new_content = content.replace(
        insert_marker,
        f'</section>\n{new_sections}\n                <section id="position">',
        1  # Only replace first occurrence
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✓ Retouched {ticker}.html")
    return True


if __name__ == "__main__":
    success_count = 0
    for ticker, data in ETFS.items():
        if retouch_file(ticker, data):
            success_count += 1
    print(f"\nDone: {success_count}/{len(ETFS)} files retouched.")
