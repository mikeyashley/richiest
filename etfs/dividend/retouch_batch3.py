#!/usr/bin/env python3
"""
Retouch script for batch 3 ETF dividend pages.
Inserts BIL-style sections after the author box.
"""

import re

ETF_DATA = {
    "dln": {
        "ticker": "DLN",
        "name": "WisdomTree U.S. LargeCap Dividend Fund",
        "short_name": "WisdomTree US LargeCap Dividend",
        "asset_class": "Equity — U.S. Large-Cap Dividend ETF",
        "strategy": "Large-Cap Dividend (dollar-weighted)",
        "payment_freq": "Monthly",
        "expense_ratio": "0.28%",
        "sponsor_name": "WisdomTree",
        "sponsor_url": "https://www.wisdomtree.com/etfs/equity/dln",
        "exchange": "AMEX",
        "bottom_line_p1": "DLN is WisdomTree's flagship large-cap dividend ETF, weighting its ~300 holdings by the dollar amount of dividends paid rather than market cap. That quirky twist tilts you toward the biggest dividend payers in the S&P universe without going all-in on the highest-yield names.",
        "bottom_line_p2": "For investors who want broad U.S. large-cap exposure with a meaningful income tilt and low turnover, DLN is a solid, cost-conscious pick. Just know that its 0.28% fee is slightly above ultra-cheap passive options, and its yield won't blow you away — it's more about quality dividend growers than headline income.",
        "pros": [
            ("Dividend-Dollar Weighting", "Allocates more to the largest dividend payers, not just the biggest companies — a smarter income tilt."),
            ("Monthly Distributions", "Pays dividends every month, making cash-flow planning easy for income-focused investors."),
            ("Broad Diversification", "Holds ~300 large-cap stocks across 11 sectors, reducing single-stock concentration risk."),
            ("Long Track Record", "Launched in 2006, DLN has navigated multiple market cycles, giving investors real performance history to evaluate."),
        ],
        "cons": [
            ("Modest Yield", "Yield typically runs 2–3%, lagging higher-yield rivals like DVY or HDV."),
            ("Higher Fee Than Passive Peers", "At 0.28%, DLN costs more than ultra-cheap dividend ETFs like VYM (0.06%)."),
            ("Tech Concentration Risk", "Technology is the largest sector weight (~20%), which can dampen income when big tech cuts dividends."),
            ("No Dividend Growth Screen", "DLN doesn't filter for dividend growers; it weights by payout size, so struggling companies can slip in."),
        ],
        "personas": [
            ("fa-chart-line", "The Income-Seeking Retiree", "You want regular monthly income from your portfolio without taking on bond-level risk. DLN's dividend-dollar weighting means your money goes where the dividends are biggest — and its 300-stock spread keeps you from being hurt by any single cut."),
            ("fa-balance-scale", "The Core Equity Diversifier", "You already hold a growth ETF like QQQ or VGT and want to balance it with something that pays you to wait. DLN adds large-cap quality with a monthly income stream that offsets growth-focused volatility."),
            ("fa-seedling", "The Long-Term Compounders", "You're reinvesting dividends and thinking in decades. DLN's focus on established dividend-paying companies with strong fundamentals gives your DRIP plan solid material to work with over time."),
        ],
        "scenarios": [
            ("Monthly Cash Flow Without Bond Risk", "A pre-retiree with $250k moves a portion of bonds into DLN to keep monthly income flowing while staying invested in large-cap U.S. equities rather than locked into fixed-income duration risk."),
            ("Rebalancing Into Quality During Volatility", "During a market pullback, an investor shifts proceeds from trimmed growth positions into DLN, collecting monthly dividends while waiting for their conviction names to reset to better valuations."),
        ],
        "comp_etf1_ticker": "VYM",
        "comp_etf1_name": "Vanguard High Dividend Yield ETF",
        "comp_etf1_why": "Lower fee (0.06%), market-cap weighted, higher yield (~3%). Great for pure yield-hunters.",
        "comp_etf2_ticker": "HDV",
        "comp_etf2_name": "iShares Core High Dividend ETF",
        "comp_etf2_why": "Higher yield focus (~3.5%), quality screen, fewer holdings (~75). Better for concentrated income plays.",
        "dln_why": "Best if you want dividend-dollar weighting logic, monthly income, and broad diversification at a reasonable cost.",
        "verdict": "DLN earns its place as a steady, sensible large-cap dividend ETF. It's not the highest yield, nor the cheapest, but its unique dollar-weighted methodology and broad diversification make it a dependable income builder. If monthly dividends from quality large-cap stocks fits your plan, DLN is a sound choice.",
        "verdict_cta": "For long-term dividend investors who appreciate methodology over marketing, DLN rewards patience. Start small, reinvest dividends, and let the compounding do its job.",
    },
    "don": {
        "ticker": "DON",
        "name": "WisdomTree U.S. MidCap Dividend Fund",
        "short_name": "WisdomTree US MidCap Dividend",
        "asset_class": "Equity — U.S. Mid-Cap Dividend ETF",
        "strategy": "Mid-Cap Dividend (dollar-weighted)",
        "payment_freq": "Monthly",
        "expense_ratio": "0.38%",
        "sponsor_name": "WisdomTree",
        "sponsor_url": "https://www.wisdomtree.com/etfs/equity/don",
        "exchange": "AMEX",
        "bottom_line_p1": "DON gives you the mid-cap corner of WisdomTree's dividend universe, weighting holdings by the dollar amount of dividends paid. Mid-cap stocks tend to sit in a sweet spot — more growth potential than large-caps, more stability than small-caps — and DON harvests dividends from the best dividend payers in that tier.",
        "bottom_line_p2": "If you're looking to diversify beyond the giant tech-heavy S&P 500 while still collecting monthly income, DON is a compelling option. Its 0.38% fee is on the higher end, but the exposure to mid-cap dividend payers is genuinely differentiated from most large-cap-dominated income ETFs.",
        "pros": [
            ("Mid-Cap Growth + Income", "Blends the income stability of dividends with the higher long-term growth potential of mid-cap companies."),
            ("Dollar-Weighted Methodology", "Allocates more to the biggest dividend payers, not just the biggest companies by market cap."),
            ("Monthly Distributions", "Regular monthly income makes it easy to plan around for retirees or income investors."),
            ("Low Correlation to Large-Cap ETFs", "Mid-cap exposure diversifies away from mega-cap tech concentration found in most equity ETFs."),
        ],
        "cons": [
            ("Higher Expense Ratio", "At 0.38%, DON is more expensive than most passive large-cap alternatives."),
            ("Modest Yield", "Mid-cap dividend yields tend to be lower than high-yield large-cap funds; DON typically yields around 2.5–3%."),
            ("More Volatility Than Large-Caps", "Mid-cap stocks experience wider price swings, which can feel uncomfortable in downturns."),
            ("Less Familiar Holdings", "Unlike large-cap funds with household names, DON's holdings are less recognizable, making due diligence harder."),
        ],
        "personas": [
            ("fa-expand-arrows-alt", "The Diversification Seeker", "Your portfolio is dominated by S&P 500 ETFs and you know it. DON plugs a real gap — mid-cap dividend payers — without forcing you to pick individual stocks."),
            ("fa-hand-holding-usd", "The Income Builder", "You want income from companies that aren't just dividend legends but solid mid-tier businesses with room to grow their payouts. DON delivers that every month."),
            ("fa-chess-knight", "The Tactical Rebalancer", "During periods when large-caps look expensive, DON gives you a place to rotate into mid-cap quality with an income cushion to buffer any short-term bumps."),
        ],
        "scenarios": [
            ("Adding Mid-Cap Income to a Large-Cap Portfolio", "An investor with a VYM + SCHD core adds DON to get mid-cap dividend exposure, reducing concentration in mega-cap financials and tech while keeping the monthly income cadence."),
            ("Rebalancing Away From Growth", "After a tech-heavy rally, a growth investor trims QQQ and parks the proceeds in DON to collect mid-cap dividends while waiting for better growth entry points."),
        ],
        "comp_etf1_ticker": "DLN",
        "comp_etf1_name": "WisdomTree U.S. LargeCap Dividend Fund",
        "comp_etf1_why": "Same WisdomTree methodology but in large-caps. Lower fee (0.28%), more stability, larger companies.",
        "comp_etf2_ticker": "VYM",
        "comp_etf2_name": "Vanguard High Dividend Yield ETF",
        "comp_etf2_why": "Cheaper (0.06%), higher yield, large-cap focused. Better if you want pure income at low cost.",
        "dln_why": "Best for investors specifically wanting mid-cap dividend exposure with WisdomTree's dollar-weighting twist.",
        "verdict": "DON is a smart diversifier for investors over-indexed to large-cap dividend ETFs. The mid-cap dividend-dollar weighting is genuinely differentiated, the monthly income cadence is reliable, and the long track record gives you real data to work with. The 0.38% fee is the main hurdle, but the unique exposure justifies it for the right investor.",
        "verdict_cta": "If your dividend portfolio is mostly large-cap and you want genuine mid-cap income diversification, DON earns a spot. Keep position sizing modest and let monthly dividends compound steadily.",
    },
    "dvy": {
        "ticker": "DVY",
        "name": "iShares Select Dividend ETF",
        "short_name": "iShares Select Dividend",
        "asset_class": "Equity — U.S. High Dividend ETF",
        "strategy": "High Dividend Yield (dividend-weighted)",
        "payment_freq": "Quarterly",
        "expense_ratio": "0.39%",
        "sponsor_name": "iShares (BlackRock)",
        "sponsor_url": "https://www.ishares.com/us/products/239726/ISHARES-SELECT-DIVIDEND-ETF",
        "exchange": "NASDAQ",
        "bottom_line_p1": "DVY is one of the oldest and largest dividend ETFs on the market, focusing on U.S. companies with a strong history of paying high dividends. It screens for payout ratio, dividend growth, and trading volume — which means you get genuinely high-yield names, not just companies that pay a token dividend.",
        "bottom_line_p2": "The tradeoff is that DVY leans heavily into utilities, financials, and energy — sectors that can lag during tech-dominated bull markets. But if consistent high income is your goal and you're OK with sector concentration, DVY has been delivering since 2003.",
        "pros": [
            ("High Yield Focus", "One of the highest-yielding broad dividend ETFs, typically delivering 3.5–4.5% annually."),
            ("Dividend Quality Screen", "Filters for payout ratio and 5-year dividend growth history, weeding out unreliable payers."),
            ("Long Track Record", "Launched in 2003 — over two decades of data across multiple market cycles."),
            ("Quarterly Distributions", "Consistent quarterly payments are familiar and predictable for income-focused investors."),
        ],
        "cons": [
            ("Sector Concentration", "Heavy exposure to utilities (~25%) and financials, which can lag during tech bull runs."),
            ("Higher Fee", "At 0.39%, it's pricier than passive alternatives like VYM (0.06%) or SCHD (0.06%)."),
            ("Fewer Holdings (~100)", "Concentrated portfolio means individual sector downturns hit harder."),
            ("Limited Growth Potential", "High-yield focus often means slower-growing companies; don't expect much price appreciation."),
        ],
        "personas": [
            ("fa-piggy-bank", "The Income-First Retiree", "You need your portfolio to pay you regularly and predictably. DVY's high yield and long track record give you confidence that those quarterly checks will keep coming even in tough markets."),
            ("fa-shield-alt", "The Defensive Allocator", "You want to reduce equity risk without going to bonds. DVY's utility and consumer staple heavy mix offers equity participation with a defensive tilt and above-average yield."),
            ("fa-university", "The Value-Oriented Investor", "You believe in buying cash-flowing businesses at reasonable prices. DVY's dividend quality screen naturally tilts toward value stocks trading at reasonable multiples."),
        ],
        "scenarios": [
            ("Building a Retirement Income Floor", "A retiree allocates 15% of their portfolio to DVY to generate a reliable quarterly income stream from high-yielding U.S. equities, supplementing Social Security and bond ladders."),
            ("Hedging Against Tech Overexposure", "An investor heavy in QQQ and VGT uses DVY as a counterweight — when high-growth tech corrects, DVY's utility and financial holdings often hold up better."),
        ],
        "comp_etf1_ticker": "VYM",
        "comp_etf1_name": "Vanguard High Dividend Yield ETF",
        "comp_etf1_why": "Much cheaper (0.06%), more holdings (~400), slightly lower yield. Better for cost-conscious investors.",
        "comp_etf2_ticker": "SCHD",
        "comp_etf2_name": "Schwab U.S. Dividend Equity ETF",
        "comp_etf2_why": "Lower fee (0.06%), dividend growth focus, strong total return record. Better for dividend growers.",
        "dln_why": "Best for income-first investors who want high current yield, a quality screen, and a proven long-term track record.",
        "verdict": "DVY has earned its place as one of the original high-yield dividend ETFs. Its dividend quality screens, high yield, and 20+ year track record make it a credible income vehicle. The higher fee and sector concentration are real tradeoffs, but for pure income-focused investors, DVY consistently delivers.",
        "verdict_cta": "If quarterly income checks and a proven track record matter more than fee minimization, DVY belongs on your income ETF shortlist. Pair it with a growth ETF for balance.",
    },
    "fcfy": {
        "ticker": "FCFY",
        "name": "First Trust S&P 500 Diversified Free Cash Flow ETF",
        "short_name": "First Trust Free Cash Flow",
        "asset_class": "Equity — U.S. Free Cash Flow ETF",
        "strategy": "Free Cash Flow Yield (S&P 500 universe)",
        "payment_freq": "Quarterly",
        "expense_ratio": "0.60%",
        "sponsor_name": "First Trust",
        "sponsor_url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FCFY",
        "exchange": "NASDAQ",
        "bottom_line_p1": "FCFY targets S&P 500 companies with the highest free cash flow yield — essentially companies generating the most cash relative to their market value. Free cash flow is the lifeblood of dividends and buybacks, so this ETF finds companies with the financial firepower to reward shareholders, even if they don't all pay high dividends today.",
        "bottom_line_p2": "This is a more sophisticated income play than a plain dividend ETF. FCFY bets that high free cash flow yield stocks will eventually translate into higher dividends, buybacks, or price appreciation. It's a quality-and-value combination, but the 0.60% fee is high for what is essentially a rules-based index strategy.",
        "pros": [
            ("Free Cash Flow Focus", "Targets companies with strong cash generation, a leading indicator of future dividend increases and buybacks."),
            ("S&P 500 Universe", "Limits selection to established, large-cap companies — quality and liquidity are built in."),
            ("Diversified Across Sectors", "The diversified mandate prevents any single sector from dominating, unlike some high-yield ETFs."),
            ("Value + Quality Tilt", "High free cash flow yield naturally screens for undervalued, cash-rich businesses."),
        ],
        "cons": [
            ("High Expense Ratio", "At 0.60%, FCFY is expensive relative to passive dividend ETFs — drag adds up over time."),
            ("Not a Pure Income Play", "Free cash flow doesn't always equal high dividends now; some picks may prioritize buybacks or growth investment instead."),
            ("Limited Track Record", "Newer ETF with less history to evaluate across full market cycles."),
            ("Quarterly Distributions Only", "No monthly income option for investors who prefer more frequent cash flow."),
        ],
        "personas": [
            ("fa-faucet", "The Cash Flow Fundamentalist", "You believe companies that generate lots of free cash flow are the best long-term compounders. FCFY is your vehicle — you're buying the engine of shareholder returns, not just the latest dividend payment."),
            ("fa-search-dollar", "The Value Investor Hybrid", "You want growth potential with income upside. High free cash flow yield stocks often trade at discount valuations, giving you both margin of safety and the potential for dividend growth."),
            ("fa-graduation-cap", "The Sophisticated DIY Investor", "You've gone beyond simple dividend screens and want exposure to the free cash flow factor. FCFY saves you the work of screening and rebalancing the universe yourself."),
        ],
        "scenarios": [
            ("Complementing a Dividend Growth Portfolio", "An investor running SCHD as a core holding adds FCFY to capture the free-cash-flow-rich portion of the S&P 500 that SCHD might miss, broadening their quality-income exposure."),
            ("Seeking Value in Expensive Markets", "When S&P 500 valuations look stretched, a portfolio manager tilts toward FCFY — high FCF yield stocks tend to have lower P/E ratios, providing a valuation buffer in downturns."),
        ],
        "comp_etf1_ticker": "COWZ",
        "comp_etf1_name": "Pacer US Cash Cows 100 ETF",
        "comp_etf1_why": "Also free cash flow focused but uses Russell 1000 universe. Lower fee (0.49%), different sector mix.",
        "comp_etf2_ticker": "SCHD",
        "comp_etf2_name": "Schwab U.S. Dividend Equity ETF",
        "comp_etf2_why": "Lower fee (0.06%), dividend growth focus, strong total return. Better for pure income compounding.",
        "dln_why": "Best for investors who specifically want free cash flow yield as their selection factor within the S&P 500 universe.",
        "verdict": "FCFY is an interesting quality-value hybrid for investors who think free cash flow yield is the right signal to buy. The S&P 500 universe keeps quality high, but the 0.60% fee is a real headwind for long-term investors. Use it as a satellite position, not a core holding.",
        "verdict_cta": "If you believe in the free cash flow factor and want a diversified way to express it, FCFY delivers. Keep it sized appropriately given the fee drag, and pair it with lower-cost core holdings.",
    },
    "fdl": {
        "ticker": "FDL",
        "name": "First Trust Morningstar Dividend Leaders Index Fund",
        "short_name": "First Trust Morningstar Dividend Leaders",
        "asset_class": "Equity — U.S. Dividend Leaders ETF",
        "strategy": "Dividend Leaders (Morningstar screen)",
        "payment_freq": "Quarterly",
        "expense_ratio": "0.45%",
        "sponsor_name": "First Trust",
        "sponsor_url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FDL",
        "exchange": "AMEX",
        "bottom_line_p1": "FDL tracks the Morningstar Dividend Leaders Index, which selects the top 100 U.S. companies with the highest dividend yields AND a consistent history of increasing or maintaining dividends. Morningstar's screen adds a quality filter most plain high-yield ETFs skip — you have to have earned your spot.",
        "bottom_line_p2": "The result is a concentrated, high-yield, quality-screened portfolio that tilts toward financials and utilities. FDL yields more than most broad market ETFs and has Morningstar's methodology backing its selections. The 0.45% fee is the main friction point versus cheaper alternatives.",
        "pros": [
            ("Morningstar Quality Screen", "Morningstar's methodology filters for consistent dividend history, not just current high yield — weeding out yield traps."),
            ("Above-Average Yield", "Typically yields 3.5–4.5%, well above the S&P 500 average."),
            ("Established Large-Cap Names", "100-stock portfolio of well-known, dividend-paying U.S. companies."),
            ("Clear Selection Criteria", "Transparent, rules-based index methodology makes it easy to understand what you own and why."),
        ],
        "cons": [
            ("Concentrated Portfolio", "Only ~100 holdings means sector downturns hit harder than broader dividend ETFs."),
            ("Higher Fee", "At 0.45%, FDL costs significantly more than VYM or SCHD."),
            ("Sector Concentration", "Heavy weighting toward financials and utilities limits performance when those sectors lag."),
            ("Quarterly Only", "No monthly income option for investors who want more frequent distributions."),
        ],
        "personas": [
            ("fa-trophy", "The Quality-Income Investor", "You want high yield but aren't willing to sacrifice dividend consistency for it. Morningstar's leadership screen gives you confidence these aren't fly-by-night payers."),
            ("fa-coins", "The Dividend Collector", "You're building a portfolio designed to generate quarterly cash without worrying about growth. FDL's above-average yield and quality screen make every quarter reliable."),
            ("fa-user-tie", "The Conservative Wealth Builder", "You're accumulating wealth with a preference for businesses that share cash with shareholders. Dividend leaders tend to be disciplined capital allocators — the kind of companies conservative investors love."),
        ],
        "scenarios": [
            ("Replacing Bond Income With Equity Income", "A near-retiree looking to shift from low-yield bonds to higher-income equities uses FDL to capture 4%+ yield from quality large-cap payers, accepting more volatility in exchange for better income."),
            ("Building a Dividend Ladder", "An investor combines FDL (quarterly) with a monthly-payer like SCHD or DLN to create a staggered income calendar, ensuring cash hits the account in different months throughout the year."),
        ],
        "comp_etf1_ticker": "DVY",
        "comp_etf1_name": "iShares Select Dividend ETF",
        "comp_etf1_why": "Similar high-yield, quality-screened approach. Similar fee (0.39%). Longer track record with over 20 years.",
        "comp_etf2_ticker": "SCHD",
        "comp_etf2_name": "Schwab U.S. Dividend Equity ETF",
        "comp_etf2_why": "Much cheaper (0.06%), strong dividend growth record, excellent total return. Better for compounders.",
        "dln_why": "Best for investors specifically wanting Morningstar's dividend leaders methodology with quality-screened high yield.",
        "verdict": "FDL is a solid high-yield dividend ETF backed by Morningstar's credible methodology. It won't be the cheapest or most diversified option, but the quality screen and above-average yield make it a credible income vehicle for conservative investors who trust Morningstar's approach.",
        "verdict_cta": "For investors who want Morningstar's seal of approval on their dividend picks and are comfortable paying a slight fee premium for it, FDL delivers consistent, quality-screened income.",
    },
    "fdn": {
        "ticker": "FDN",
        "name": "First Trust Dow Jones Internet Index Fund",
        "short_name": "First Trust Dow Jones Internet",
        "asset_class": "Equity — U.S. Internet Sector ETF",
        "strategy": "Dow Jones Internet Composite Index",
        "payment_freq": "Annual",
        "expense_ratio": "0.52%",
        "sponsor_name": "First Trust",
        "sponsor_url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FDN",
        "exchange": "NYSE",
        "bottom_line_p1": "FDN is an internet sector ETF, not a traditional income or dividend fund. It tracks the Dow Jones Internet Composite Index, owning the largest U.S. internet companies by revenue. Think Amazon, Meta, Alphabet, Netflix — the titans of the digital economy. It's a growth vehicle wrapped in an ETF.",
        "bottom_line_p2": "Despite its placement in dividend ETF directories, FDN is primarily a capital appreciation play on the internet sector. Its yield is minimal. If you're here for income, this isn't your fund. But if you want concentrated exposure to internet growth leaders at a reasonable cost, FDN has one of the longest track records in the sector.",
        "pros": [
            ("Pure Internet Sector Exposure", "One of the few ETFs dedicated entirely to the internet ecosystem — e-commerce, social media, streaming, search."),
            ("Long Track Record", "Launched in 2006, FDN has over 15 years of data covering multiple tech boom-and-bust cycles."),
            ("Large-Cap Quality", "Focuses on the biggest, most liquid internet companies — less small-cap speculative risk."),
            ("Revenue-Based Index", "Dow Jones methodology screens for internet revenue concentration, keeping holdings genuinely internet-centric."),
        ],
        "cons": [
            ("Minimal Income", "FDN is not a dividend fund — yield is near zero. If you need income, look elsewhere."),
            ("High Volatility", "Internet stocks experience dramatic price swings; FDN can drop 40%+ in bear markets."),
            ("Concentration Risk", "Top 10 holdings often represent 60%+ of the fund — a few mega-caps dominate."),
            ("Higher Fee vs. Broad Tech ETFs", "At 0.52%, FDN costs more than QQQ (0.20%) for more concentrated, less diversified exposure."),
        ],
        "personas": [
            ("fa-globe", "The Internet Economy Bull", "You believe digital commerce, advertising, streaming, and cloud are the backbone of the next decade of growth. FDN lets you own that thesis in one ETF without picking individual stocks."),
            ("fa-rocket", "The Sector Rotator", "You run a tactical portfolio and want a clean, liquid vehicle to express a bullish internet thesis during growth-favorable markets. FDN is an easy on/off switch."),
            ("fa-layer-group", "The Thematic Diversifier", "You own broad market ETFs but want to tilt toward internet-specific growth. FDN adds sector concentration you won't get from VTI or SPY alone."),
        ],
        "scenarios": [
            ("Adding Internet Sector Exposure to a Diversified Portfolio", "A long-term investor who owns VTI as their core adds FDN as a 10% satellite position to increase exposure to internet-driven revenue growth that's underweighted in market-cap total market funds."),
            ("Tactical Play During Tech Bull Markets", "During the early stages of a rate-cutting cycle, when growth stocks historically outperform, a tactical investor increases FDN exposure to ride internet sector momentum."),
        ],
        "comp_etf1_ticker": "QQQ",
        "comp_etf1_name": "Invesco QQQ Trust",
        "comp_etf1_why": "Lower fee (0.20%), broader tech exposure (not just internet), higher AUM and liquidity. Better for general tech exposure.",
        "comp_etf2_ticker": "OGIG",
        "comp_etf2_name": "O'Shares Global Internet Giants ETF",
        "comp_etf2_why": "Adds global internet exposure (China, Europe) vs. FDN's U.S.-only focus. More diversified geographically.",
        "dln_why": "Best for investors who specifically want U.S. internet sector purity with a long historical track record.",
        "verdict": "FDN is the go-to pure-play U.S. internet ETF for investors who want clean sector exposure with a long track record. It's not an income fund — it's a growth vehicle. If you believe in the internet economy's long-term trajectory, FDN provides a proven, liquid way to own it.",
        "verdict_cta": "Use FDN as a satellite position alongside diversified core holdings. Don't expect dividends; expect volatility and the potential for significant long-run capital appreciation.",
    },
    "fthi": {
        "ticker": "FTHI",
        "name": "First Trust BuyWrite Income ETF",
        "short_name": "First Trust BuyWrite Income",
        "asset_class": "Equity — Covered Call Income ETF",
        "strategy": "BuyWrite (Covered Call on S&P 500)",
        "payment_freq": "Monthly",
        "expense_ratio": "0.70%",
        "sponsor_name": "First Trust",
        "sponsor_url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FTHI",
        "exchange": "NASDAQ",
        "bottom_line_p1": "FTHI is an actively managed covered call ETF that owns S&P 500 stocks and writes call options on the index to generate extra income. The options premium gets paid out as monthly distributions, which is why FTHI typically yields significantly more than a plain S&P 500 fund.",
        "bottom_line_p2": "The catch: by selling calls, you cap your upside in strong bull markets. FTHI will underperform the S&P 500 when stocks run hard, but it provides enhanced income and some cushion during flat or mildly down markets. Think of it as trading growth potential for income certainty — a classic tradeoff for income-oriented investors.",
        "pros": [
            ("Enhanced Monthly Income", "Covered call premiums boost distributions well above what traditional dividend ETFs pay — often 5–8% yield."),
            ("Active Management", "First Trust's team actively manages the call writing strategy to optimize premium capture."),
            ("S&P 500 Underlying Exposure", "Core portfolio tracks large-cap U.S. equities, providing solid equity market participation."),
            ("Monthly Distributions", "Regular monthly payouts make cash flow planning predictable and frequent."),
        ],
        "cons": [
            ("Capped Upside", "Selling call options caps gains during strong bull markets — you'll lag the S&P 500 when stocks surge."),
            ("High Expense Ratio", "At 0.70%, FTHI is expensive and active management fees eat into net returns."),
            ("Complex Strategy", "Options overlays are harder to understand and evaluate than plain equity ETFs."),
            ("Return of Capital Risk", "Some monthly distributions may include return of capital, reducing your cost basis rather than being pure income."),
        ],
        "personas": [
            ("fa-hand-holding-usd", "The Income Maximizer", "You need high monthly income from your portfolio and are OK trading away some upside for it. FTHI's covered call strategy delivers regular premiums that plain dividend ETFs can't match."),
            ("fa-chart-bar", "The Tactical Income Investor", "You're bullish on the stock market but not expecting explosive returns. In sideways or modestly rising markets, FTHI's premium collection shines relative to both stocks and bonds."),
            ("fa-umbrella", "The Conservative Equity Holder", "You want equity market exposure but hate watching your account drop hard. The premium income cushions mild downturns and the S&P 500 core gives you meaningful participation when markets recover."),
        ],
        "scenarios": [
            ("Generating Income in a Sideways Market", "An investor expecting muted equity returns for 12–18 months shifts a portion of their S&P 500 holdings into FTHI to collect monthly option premiums while keeping equity exposure intact."),
            ("Building a High-Income Retirement Portfolio", "A retiree combines FTHI with bond ETFs to create a high-income portfolio that generates 5–7% annually — far above what a standard dividend ETF or bond ladder alone would provide."),
        ],
        "comp_etf1_ticker": "XYLD",
        "comp_etf1_name": "Global X S&P 500 Covered Call ETF",
        "comp_etf1_why": "Similar covered call strategy, lower fee (0.60%), passive approach. Well-known covered call benchmark ETF.",
        "comp_etf2_ticker": "JEPI",
        "comp_etf2_name": "JPMorgan Equity Premium Income ETF",
        "comp_etf2_why": "Lower volatility, uses ELNs not direct calls, higher AUM, strong track record. Many investors prefer JEPI's smoother ride.",
        "dln_why": "Best for investors who specifically want First Trust's active management on the covered call strategy with S&P 500 underlying.",
        "verdict": "FTHI delivers on its core promise: enhanced monthly income from a covered call strategy on S&P 500 stocks. The 0.70% fee is the main drawback, and investors must genuinely accept capped upside in exchange. In income-focused portfolios or during sideways markets, FTHI earns its place.",
        "verdict_cta": "If high monthly income matters more to you than maxing out bull market gains, FTHI is worth owning. Pair it with pure equity exposure elsewhere so you're not entirely capping your portfolio's growth.",
    },
    "ftqi": {
        "ticker": "FTQI",
        "name": "First Trust Nasdaq BuyWrite Income ETF",
        "short_name": "First Trust Nasdaq BuyWrite Income",
        "asset_class": "Equity — Covered Call Income ETF",
        "strategy": "BuyWrite (Covered Call on Nasdaq-100)",
        "payment_freq": "Monthly",
        "expense_ratio": "0.75%",
        "sponsor_name": "First Trust",
        "sponsor_url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FTQI",
        "exchange": "NASDAQ",
        "bottom_line_p1": "FTQI is FTHI's tech-heavy sibling — a covered call ETF that owns Nasdaq-100 stocks and writes call options to generate monthly income. Because Nasdaq-100 stocks tend to have higher implied volatility, the options premiums are richer, which means FTQI can potentially generate even more income than its S&P 500 counterpart.",
        "bottom_line_p2": "But this comes at a real cost: Nasdaq-100 stocks are growth-oriented and often don't pay big dividends themselves, so FTQI's yield comes almost entirely from option premiums. The 0.75% fee is high, and the upside cap can be particularly painful during technology-led bull runs. It's an income tool, not a growth vehicle.",
        "pros": [
            ("Higher Potential Income", "Nasdaq-100's higher implied volatility generates richer call premiums — potentially higher yield than S&P 500 covered call ETFs."),
            ("Tech Sector Exposure", "Underlying Nasdaq-100 holdings give you participation in top tech and growth names."),
            ("Monthly Distributions", "Regular monthly income from option premiums, paid directly to investors."),
            ("Active Management", "First Trust actively manages the call-writing to optimize premium income."),
        ],
        "cons": [
            ("Significant Upside Cap", "Nasdaq-100 can rocket in growth markets; selling calls means you leave enormous gains on the table."),
            ("Highest Fee in the Group", "At 0.75%, FTQI is expensive even among covered call ETFs."),
            ("Tech Concentration Risk", "Heavy Nasdaq-100 exposure means big drawdowns when tech sells off hard, with limited premium cushion."),
            ("Complex Tax Treatment", "Option premium income and potential return-of-capital distributions create complicated tax situations."),
        ],
        "personas": [
            ("fa-bolt", "The Tech-Income Hybrid", "You love tech stocks but want them to generate consistent monthly income rather than just sitting there waiting for appreciation. FTQI lets tech pay you every month via option premiums."),
            ("fa-shield-alt", "The Volatility Monetizer", "You know tech is volatile. Instead of fighting it, you're collecting premiums from that volatility. FTQI turns the Nasdaq's wild swings into monthly income deposits."),
            ("fa-balance-scale", "The Portfolio Income Enhancer", "Your portfolio is heavy on growth but light on income. FTQI adds monthly cash flow without forcing you to sell your growth allocation or load up on bonds."),
        ],
        "scenarios": [
            ("Extracting Income From Tech Exposure", "An investor already overweight in tech stocks via QQQ uses FTQI as a replacement — same underlying exposure, but with monthly income generated by option premiums on the position."),
            ("Income in a High-Volatility Environment", "During periods of elevated market volatility (VIX above 20), FTQI's option premiums swell, generating above-average monthly distributions — exactly when income stability matters most."),
        ],
        "comp_etf1_ticker": "QYLD",
        "comp_etf1_name": "Global X Nasdaq 100 Covered Call ETF",
        "comp_etf1_why": "Very similar strategy, lower fee (0.60%), passive. QYLD is one of the most popular Nasdaq covered call ETFs.",
        "comp_etf2_ticker": "JEPQ",
        "comp_etf2_name": "JPMorgan Nasdaq Equity Premium Income ETF",
        "comp_etf2_why": "Uses ELNs for smoother income, lower volatility drawdowns, strong track record. Many prefer JEPQ's balance.",
        "dln_why": "Best for investors wanting First Trust's active covered call management on a Nasdaq-100 underlying portfolio.",
        "verdict": "FTQI is a specialized income tool for investors who want their tech exposure to generate monthly cash. The higher implied vol of Nasdaq stocks is a genuine premium source. But the 0.75% fee and severe upside cap mean FTQI should be a tactical, income-focused position — not a growth vehicle.",
        "verdict_cta": "Use FTQI in income-focused portfolios where monthly cash flow matters more than maximum long-run returns. Size it modestly and ensure you have pure-growth tech exposure elsewhere in your portfolio.",
    },
    "fvd": {
        "ticker": "FVD",
        "name": "First Trust Value Line Dividend Index Fund",
        "short_name": "First Trust Value Line Dividend",
        "asset_class": "Equity — U.S. Dividend + Safety ETF",
        "strategy": "Value Line Dividend Index (safety + dividend)",
        "payment_freq": "Monthly",
        "expense_ratio": "0.70%",
        "sponsor_name": "First Trust",
        "sponsor_url": "https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FVD",
        "exchange": "NYSE",
        "bottom_line_p1": "FVD is a genuinely unique dividend ETF — it uses Value Line's proprietary safety rankings to screen out risky dividend payers before selecting high-yield stocks. Value Line is one of the oldest, most respected independent stock research firms, and their Safety Rank 1 or 2 requirement adds a layer of quality control you rarely see in dividend ETFs.",
        "bottom_line_p2": "The result is a defensively oriented, dividend-focused portfolio that tilts toward utilities, consumer staples, and financials. FVD typically yields 2.5–4% with low volatility relative to peers. The 0.70% fee is the main headwind, but the Value Line safety overlay is a genuine differentiator.",
        "pros": [
            ("Value Line Safety Screen", "Unique methodology requiring Value Line Safety Rank 1 or 2 before a stock is eligible — weeds out financially fragile dividend payers."),
            ("Monthly Distributions", "Consistent monthly income for investors who prefer frequent cash flow."),
            ("Defensive Orientation", "Utility and consumer staples tilt makes FVD resilient in market downturns."),
            ("Broad Diversification", "200+ holdings spread across sectors provide ample diversification within the dividend universe."),
        ],
        "cons": [
            ("High Expense Ratio", "At 0.70%, FVD is expensive relative to plain passive dividend ETFs."),
            ("Lag During Bull Markets", "Defensive and utility-heavy positioning means FVD trails in strong equity rallies."),
            ("Value Line Dependency", "The fund's quality depends entirely on Value Line's safety rankings — a black-box input most investors can't independently verify."),
            ("Lower Yield Than High-Yield Peers", "Safety screen keeps out some of the highest-yielding (but riskier) dividend payers."),
        ],
        "personas": [
            ("fa-hard-hat", "The Capital Preservation Investor", "You care as much about not losing money as you do about earning income. FVD's Value Line safety screen gives you confidence that your dividend stocks won't implode while you're collecting checks."),
            ("fa-home", "The Conservative Retiree", "Volatility keeps you up at night. FVD's defensive sector tilt and safety-first methodology make it one of the calmer dividend ETFs — income without the sleepless nights."),
            ("fa-leaf", "The Steady Compounder", "You're reinvesting FVD's monthly dividends over a long time horizon. Value Line's methodology keeps your compounding engine full of quality businesses that are unlikely to cut dividends unexpectedly."),
        ],
        "scenarios": [
            ("Replacing CD Income With a Safer Equity Alternative", "A conservative investor rolling off a CD ladder shifts into FVD to maintain monthly income at a higher yield than current CD rates, while accepting mild equity volatility they're comfortable with."),
            ("Defensive Rebalancing During Late-Cycle Markets", "As economic indicators soften, an investor increases FVD allocation to shift toward defensive quality dividend payers that historically hold up better during recessions."),
        ],
        "comp_etf1_ticker": "VYM",
        "comp_etf1_name": "Vanguard High Dividend Yield ETF",
        "comp_etf1_why": "Much cheaper (0.06%), broader, higher yield. Better for cost-conscious investors who don't need the safety overlay.",
        "comp_etf2_ticker": "NOBL",
        "comp_etf2_name": "ProShares S&P 500 Dividend Aristocrats ETF",
        "comp_etf2_why": "Dividend growth focus (25+ years of increases), lower fee (0.35%). Better for dividend growth compounders.",
        "dln_why": "Best for investors who specifically want Value Line's safety ranking as a quality screen on top of dividend selection.",
        "verdict": "FVD is a thoughtfully constructed defensive dividend ETF with a genuinely unique quality overlay. The Value Line safety screen is its key differentiator — if you believe in Value Line's methodology, FVD gives you a safe, income-producing portfolio. The 0.70% fee is its biggest obstacle against cheaper alternatives.",
        "verdict_cta": "If safety-first dividend investing is your style and you trust Value Line's time-tested methodology, FVD earns a spot in a conservative income portfolio. Keep sizing in check given the fee.",
    },
    "hdv": {
        "ticker": "HDV",
        "name": "iShares Core High Dividend ETF",
        "short_name": "iShares Core High Dividend",
        "asset_class": "Equity — U.S. High Dividend ETF",
        "strategy": "Morningstar Dividend Yield Focus Index",
        "payment_freq": "Quarterly",
        "expense_ratio": "0.08%",
        "sponsor_name": "iShares (BlackRock)",
        "sponsor_url": "https://www.ishares.com/us/products/239566/ISHARES-CORE-HIGH-DIVIDEND-ETF",
        "exchange": "NYSE",
        "bottom_line_p1": "HDV is iShares' answer to the high-yield dividend ETF question — and it's one of the best deals in the space. At just 0.08% annual expense ratio, you get Morningstar's Dividend Yield Focus Index, which screens for high yield AND financial health, eliminating the dividend traps that plague cheaper yield-chasing.",
        "bottom_line_p2": "The result is a concentrated (~75 holdings), high-quality, high-yield portfolio dominated by energy, healthcare, and consumer staples. HDV typically yields 3.5–4.5% while keeping fees near-zero. It's not a diversification machine, but for straightforward high income from quality companies at minimal cost, HDV is hard to beat.",
        "pros": [
            ("Ultra-Low Fee", "At 0.08%, HDV is one of the cheapest high-yield dividend ETFs available — near-zero fee drag."),
            ("Morningstar Quality Screen", "Screens for financial health before selecting high-yield stocks, minimizing dividend trap risk."),
            ("High Current Yield", "Typically yields 3.5–4.5%, well above S&P 500 average — genuine income from day one."),
            ("iShares / BlackRock Brand", "World's largest ETF provider — massive AUM, excellent liquidity, tight spreads."),
        ],
        "cons": [
            ("Concentrated Portfolio (~75 stocks)", "Fewer holdings than broader dividend ETFs means more sector concentration risk."),
            ("Sector Concentration", "Energy and healthcare represent large chunks — performance tied heavily to these two sectors."),
            ("Quarterly Distributions Only", "No monthly income option for investors who prefer more frequent cash flow."),
            ("Limited Growth Potential", "High-yield focus skews toward mature, slower-growing businesses — don't expect much price appreciation."),
        ],
        "personas": [
            ("fa-dollar-sign", "The Yield-Maximizing Income Investor", "You want the highest possible quality-screened yield at the lowest possible cost. HDV nails this combination: Morningstar's methodology, above-average yield, and a fee that's essentially free."),
            ("fa-shield-alt", "The Defensive Income Seeker", "Energy, healthcare, and consumer staples are your comfort zone. HDV's natural sector tilt gives you defensive exposure that often holds up when growth stocks stumble."),
            ("fa-gem", "The Cost-Conscious Dividend Investor", "You've done the math on fee drag and you want premium income without paying for it. At 0.08%, HDV lets you keep 99.92% of your returns — every dollar matters over decades."),
        ],
        "scenarios": [
            ("Core High-Income Position at Minimal Cost", "A retiree builds their equity income portfolio around HDV as the high-yield core, combining it with SCHD for dividend growth and a bond ETF for stability — all at very low total cost."),
            ("Tilting a Portfolio Toward Defensive Income", "An investor reducing growth exposure during late economic cycles adds HDV to shift toward defensive, cash-generating businesses (energy majors, healthcare giants, consumer staples) that historically weather downturns well."),
        ],
        "comp_etf1_ticker": "DVY",
        "comp_etf1_name": "iShares Select Dividend ETF",
        "comp_etf1_why": "More holdings, similar yield, but much higher fee (0.39%). Also iShares-branded but pricier.",
        "comp_etf2_ticker": "VYM",
        "comp_etf2_name": "Vanguard High Dividend Yield ETF",
        "comp_etf2_why": "Also very cheap (0.06%), more holdings (~400), slightly lower yield. Broader, less concentrated alternative.",
        "dln_why": "Best for investors wanting high yield + Morningstar quality screen at near-zero cost — hard to argue against at 0.08%.",
        "verdict": "HDV is one of the clearest value propositions in dividend ETF investing: Morningstar quality screening, high current yield, and iShares' scale — all for 0.08% per year. The sector concentration is a real tradeoff, but for investors who want quality high-yield income at minimal cost, HDV is a top-tier choice.",
        "verdict_cta": "If you want a low-cost, quality-screened, high-yield dividend ETF from the world's most trusted ETF provider, HDV deserves a position in your income portfolio. Simple, effective, and cheap.",
    },
}


def build_new_sections(d: dict) -> str:
    ticker = d["ticker"]
    name = d["name"]
    asset_class = d["asset_class"]
    strategy = d["strategy"]
    payment_freq = d["payment_freq"]
    expense_ratio = d["expense_ratio"]
    sponsor_name = d["sponsor_name"]
    sponsor_url = d["sponsor_url"]
    exchange = d["exchange"]

    pros_rows = "\n".join(
        f"""                                <tr>
                                    <td><strong>{p[0]}:</strong> {p[1]}</td>
                                    <td><strong>{c[0]}:</strong> {c[1]}</td>
                                </tr>"""
        for p, c in zip(d["pros"], d["cons"])
    )

    persona_boxes = "\n".join(
        f"""                    <div class="persona-box">
                        <h3><i class="fas {p[0]}"></i> {p[1]}</h3>
                        <p>{p[2]}</p>
                    </div>"""
        for p in d["personas"]
    )

    scenario_bullets = "\n".join(
        f"""                        <li>
                            <p><strong>{s[0]}:</strong> {s[1]}</p>
                        </li>"""
        for s in d["scenarios"]
    )

    c1 = d["comp_etf1_ticker"]
    c1_name = d["comp_etf1_name"]
    c1_why = d["comp_etf1_why"]
    c2 = d["comp_etf2_ticker"]
    c2_name = d["comp_etf2_name"]
    c2_why = d["comp_etf2_why"]
    dln_why = d["dln_why"]

    sections = f"""
                <section id="bottom-line" class="section-grey">
                    <div class="summary-box">
                        <h2>The Bottom Line Up Front</h2>
                        <p><strong>Quick take:</strong> {d["bottom_line_p1"]}</p>
                        <p>{d["bottom_line_p2"]}</p>
                    </div>
                </section>

                <section id="overview" class="section-white">
                    <h2>{ticker} Explained</h2>
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
                                    <td>{ticker}</td>
                                    <td>{asset_class}</td>
                                    <td>{strategy}</td>
                                    <td>{payment_freq}</td>
                                    <td>{expense_ratio}</td>
                                    <td><a href="{sponsor_url}" target="_blank" rel="noopener noreferrer">{sponsor_name}</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <section id="pros-cons" class="section-grey">
                    <h2>{ticker}: The Good, The Bad, and The Honest</h2>
                    <div class="table-container">
                        <table class="pros-cons-table">
                            <thead>
                                <tr>
                                    <th class="w-50">Pros <i class="fas fa-check-circle green-check"></i></th>
                                    <th class="w-50">Cons <i class="fas fa-times-circle red-x"></i></th>
                                </tr>
                            </thead>
                            <tbody>
{pros_rows}
                            </tbody>
                        </table>
                    </div>
                </section>

                <section id="who-should-buy" class="section-white">
                    <h2>Who Should Consider {ticker}?</h2>
{persona_boxes}
                </section>

                <section id="scenarios" class="section-grey">
                    <h2>{ticker} in Action: Real-World Scenarios</h2>
                    <ul>
{scenario_bullets}
                    </ul>
                </section>

                <section id="comparison" class="section-white">
                    <h2>{ticker} vs. The Competition</h2>
                    <div class="table-container text-center mb-4">
                        <table class="etf-comparison-table">
                            <thead>
                                <tr>
                                    <th>Feature</th>
                                    <th>{ticker} ({name})</th>
                                    <th>{c1} ({c1_name})</th>
                                    <th>{c2} ({c2_name})</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Why You Might Pick It</strong></td>
                                    <td>{dln_why}</td>
                                    <td>{c1_why}</td>
                                    <td>{c2_why}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <section id="final-verdict" class="section-grey">
                    <div class="final-verdict-box">
                        <h2>The Richiest.com Final Verdict: Is {ticker} Right For You?</h2>
                        <p>{d["verdict"]}</p>
                        <p>{d["verdict_cta"]}</p>
                    </div>
                </section>
"""
    return sections


# Insertion anchor - right after the author box section closes and before section id="position"
AUTHOR_SECTION_CLOSE = """                </section>
                <section id="position">"""

for ticker_key, data in ETF_DATA.items():
    filepath = f"/Users/michael/Documents/GitHub/richiest/etfs/dividend/{ticker_key}.html"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_sections = build_new_sections(data)
    replacement = f"""                </section>
{new_sections}
                <section id="position">"""

    if AUTHOR_SECTION_CLOSE in content:
        new_content = content.replace(AUTHOR_SECTION_CLOSE, replacement, 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ {ticker_key}.html — inserted sections")
    else:
        print(f"❌ {ticker_key}.html — anchor not found, skipping")

print("Done!")
