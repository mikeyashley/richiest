#!/usr/bin/env python3
"""
Script to restructure ETF HTML files to have exactly 10 sections:
1. #bottom-line (section-grey)
2. #overview (section-white)
3. #pros-cons (section-grey)
4. #who-should-buy (section-white)
5. #price (section-grey)
6. #technical-details (section-white)
7. #chart (section-grey)
8. #comparison (section-white)
9. #final-verdict (section-grey)
10. #disclaimer (small-text-section section-grey)
"""

import os
import re
import sys
from pathlib import Path

# Get the ETF directory from command line
ETF_DIR = sys.argv[1] if len(sys.argv) > 1 else "/Users/michael/Documents/GitHub/richiest/etfs"

class ETFReformatter:
    def __init__(self, etf_dir):
        self.etf_dir = Path(etf_dir)
        self.author_image_url = "https://firebasestorage.googleapis.com/v0/b/makemoney-2eb29.appspot.com/o/AI%2Fauthor_MichaelAshley.jpg?alt=media&token=b98d7e8f-db82-4993-b39e-a5dc80cc7857"
        self.ticker = None

    def get_ticker_from_filename(self, filepath):
        """Extract ticker from filename (e.g., ddm.html -> DDM)"""
        return Path(filepath).stem.upper()

    def extract_title(self, content):
        """Extract the title from the HTML"""
        match = re.search(r'<title>([^<]+)</title>', content)
        if match:
            return match.group(1).strip()
        return "ETF"

    def extract_etf_name(self, content):
        """Extract ETF name from hero section"""
        match = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
        if match:
            return match.group(1).strip()
        return "ETF"

    def extract_etf_sub(self, content):
        """Extract ETF subtitle from hero section"""
        match = re.search(r'<p class="etf-hero-sub">([^<]+)</p>', content)
        if match:
            return match.group(1).strip()
        return "ETF overview and analysis."

    def extract_etf_eyebrow(self, content):
        """Extract ETF eyebrow category"""
        match = re.search(r'<p class="etf-hero-eyebrow">([^<]+)</p>', content)
        if match:
            return match.group(1).strip()
        return "ETFs"

    def create_bottom_line(self, ticker, name, sub):
        """Create the bottom-line section"""
        return f'''                <section id="bottom-line" class="section-grey">
                    <div class="summary-box">
                        <h2>The Bottom Line Up Front</h2>
                        <p><strong>Quick take:</strong> {ticker} is a focused ETF designed to deliver targeted market exposure through its specific investment strategy.</p>
                        <p><strong>{ticker}</strong> ({name})</p>
                        <p>{sub}</p>
                    </div>
                    <p class="page-disclosure" style="font-size: 0.85rem; margin-top: 12px;">This content is for informational and educational purposes only and is not personalized investment advice.</p>
                </section>
'''

    def create_overview(self, ticker, name, sub):
        """Create the overview section"""
        return f'''                <section id="overview" class="section-white">
                    <h2>{ticker} Explained: What It Is and Why It Matters</h2>
                    <p>{ticker} ({name}) is an exchange-traded fund that provides targeted exposure to its chosen market segment or investment strategy. This ETF is designed to track a specific index, sector, or asset class, offering investors a transparent and efficient way to gain market exposure.</p>
                    <p> ETFs like {ticker} are popular among investors seeking:</p>
                    <ul>
                        <li><strong>Market exposure:</strong> Gain access to a diversified basket of securities in a single trade.</li>
                        <li><strong>Liquidity:</strong> Trade throughout the day like a stock, with real-time pricing.</li>
                        <li><strong>Transparency:</strong> Daily disclosure of holdings for full visibility into your investment.</li>
                        <li><strong>Cost efficiency:</strong> Typically lower expense ratios compared to actively managed funds.</li>
                    </ul>
                    <p>{ticker} is managed by a leading ETF sponsor, combining rigorous index replication with strong operational infrastructure.</p>

                    <div class="methodology-box">
                        <p class="methodology-note"><strong>Methodology note:</strong> This review combines sponsor materials, public fund documents, market data, and editorial analysis. Holdings, yields, expense ratios, and distributions can change over time, so verify current details with the fund sponsor before making decisions.</p>
                    </div>

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
                                    <td>Equity ETF</td>
                                    <td>Passive Index Tracking</td>
                                    <td>Quarterly</td>
                                    <td>0.08% - 0.50%</td>
                                    <td><a href="https://www.ssga.com/us/en/individual/etfs" target="_blank" rel="noopener noreferrer">SSGA</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
'''

    def create_pros_cons(self, ticker):
        """Create the pros-cons section"""
        return f'''                <section id="pros-cons" class="section-grey">
                    <h2>{ticker}: The Good, The Bad, and The Steady</h2>
                    <p>Every investment has its strengths and weaknesses. Here's what makes {ticker} a standout for some, and a miss for others.</p>
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
                                    <td><strong>Targeted Exposure:</strong> Direct access to a specific market segment or investment theme.</td>
                                    <td><strong>Market Risk:</strong> Value fluctuates with the underlying index or sector.</td>
                                </tr>
                                <tr>
                                    <td><strong>Diversification:</strong> Instant diversification across multiple securities within one trade.</td>
                                    <td><strong>Liquidity varies:</strong> Some ETFs have lower trading volumes, affecting bid-ask spreads.</td>
                                </tr>
                                <tr>
                                    <td><strong>Transparency:</strong> Holdings disclosed daily for full visibility.</td>
                                    <td><strong>Tracking error:</strong> Performance may deviate slightly from the underlying index.</td>
                                </tr>
                                <tr>
                                    <td><strong>Cost Efficiency:</strong> Typically lower fees than actively managed funds.</td>
                                    <td><strong>Tax considerations:</strong> Capital gains distributions may have tax implications.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
'''

    def create_who_should_buy(self, ticker):
        """Create the who-should-buy section"""
        return f'''                <section id="who-should-buy" class="section-white">
                    <h2>Who Should Consider {ticker}?</h2>
                    <p>{ticker} makes the most sense when you want targeted exposure to a specific market segment, sector, or investment strategy. It's designed for investors looking to complement their portfolio with focused market access.</p>
                    <p><strong>Best for:</strong> investors seeking targeted market exposure, sector rotation, or thematic investing.<br>
                        <strong>Not ideal for:</strong> investors who need broad market diversification or long-term capital appreciation from a single holding.<br>
                        <strong>Main tradeoff:</strong> you gain focused exposure but give up the broad diversification of total market funds.</p>

                    <div class="persona-box">
                        <h3><i class="fas fa-target"></i> Sector Rotation Strategy</h3>
                        <p>Use {ticker} as part of a rotation strategy to capitalize on changing market conditions. When a particular sector looks attractive, {ticker} provides direct exposure without individual stock selection risk.</p>
                    </div>

                    <div class="persona-box">
                        <h3><i class="fas fa-balance-scale"></i> Portfolio Balance</h3>
                        <p>Add {ticker} to complement your core holdings. It can help you fine-tune your market exposure and take advantage of specific sector opportunities while maintaining a diversified base.</p>
                    </div>

                    <div class="persona-box">
                        <h3><i class="fas fa-chart-line"></i> Tactical Allocation</h3>
                        <p>Use {ticker} for tactical positioning when market conditions suggest a particular segment may outperform. The intraday tradability allows you to adjust your exposure quickly.</p>
                    </div>

                    <h3>Common Use Cases</h3>
                    <ul>
                        <li><strong>Building a thematic portfolio:</strong> Combine multiple sector or theme-focused ETFs to build your market exposure.</li>
                        <li><strong>Market rotation:</strong> Shift exposure between sectors based on your market outlook.</li>
                        <li><strong>Complementing core holdings:</strong> Add targeted exposure to supplement broad market funds.</li>
                    </ul>
                </section>
'''

    def create_price(self, ticker):
        """Create the price section"""
        return f'''                <section id="price" class="section-grey">
                    <h2>{ticker} - Price / Yield</h2>
                    <div class="chart-container">
                        <h4>Current market snapshot</h4>
                        <div class="chart">
                            <script type="text/javascript"
                                src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js"
                                async> {{"symbol": "AMEX:{ticker}", "width": "100%", "locale": "en", "colorTheme": "light", "isTransparent": false}} </script>
                        </div>
                    </div>
                </section>
'''

    def create_technical_details(self, ticker, name):
        """Create the technical-details section"""
        return f'''                <section id="technical-details" class="section-white">
                    <h2>{ticker} Technical Details</h2>
                    <p>{ticker} ({name}) trades on a major U.S. exchange and tracks its target index through a passive indexing approach. The ETF is structured as an open-end fund, offering continuous creation and redemption of shares.</p>
                    <div class="table-container mb-4">
                        <table>
                            <tbody>
                                <tr>
                                    <td><strong>Ticker Symbol</strong></td>
                                    <td>{ticker}</td>
                                </tr>
                                <tr>
                                    <td><strong>Exchange</strong></td>
                                    <td>NYSE Arca / NASDAQ</td>
                                </tr>
                                <tr>
                                    <td><strong>Inception Date</strong></td>
                                    <td>Various (check fund sponsor)</td>
                                </tr>
                                <tr>
                                    <td><strong>Assets Under Management (AUM)</strong></td>
                                    <td>$100M - $10B+ (varies by ETF)</td>
                                </tr>
                                <tr>
                                    <td><strong>Underlying Index</strong></td>
                                    <td>Specific index (varies by ETF)</td>
                                </tr>
                                <tr>
                                    <td><strong>Credit Quality</strong></td>
                                    <td>N/A (Equity ETF)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <h3>Understanding {ticker}'s Income</h3>
                    <p>While {ticker} may distribute dividends or interest payments, the primary focus is on market exposure and capital appreciation. Distributions are typically reinvested or paid quarterly.</p>
                    <p>For the most current yield, distribution history, and official fund documents, use the sponsor page:</p>
                    <p><a href="https://www.ssga.com/us/en/individual/etfs" target="_blank" rel="noopener noreferrer" class="external-link">Visit the Official ETF Fund Page <i class="fas fa-external-link-alt"></i></a></p>
                </section>
'''

    def create_chart(self, ticker):
        """Create the chart section"""
        return f'''                <section id="chart" class="section-grey">
                    <h2>{ticker} - Chart</h2>
                    <div class="chart-container">
                        <h4>Price action over time</h4>
                        <div class="chart">
                            <script type="text/javascript"
                                src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
                                    {{"autosize": true, "symbol": "AMEX:{ticker}", "interval": "3M", "timezone": "America/New_York", "theme": "light", "style": "2", "locale": "en", "allow_symbol_change": false, "calendar": false, "support_host": "https://www.tradingview.com"}}
                                </script>
                        </div>
                    </div>
                </section>
'''

    def create_comparison(self, ticker):
        """Create the comparison section"""
        return f'''                <section id="comparison" class="section-white">
                    <h2>{ticker} vs. The Competition: A Quick Look</h2>
                    <p>The real decision is not whether {ticker} is "good" in the abstract. It is whether {ticker} fits your specific market exposure needs and investment strategy.</p>
                    <p><strong>{ticker}</strong> is usually the cleanest fit for investors who want targeted exposure to its specific market segment. If you are looking for different exposure or fee structure, other ETFs in the same category may make sense.</p>
                    <div class="table-container text-center mb-4">
                        <table class="etf-comparison-table">
                            <thead>
                                <tr>
                                    <th>Feature</th>
                                    <th>{ticker}</th>
                                    <th>Similar ETF 1</th>
                                    <th>Similar ETF 2</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>What it holds</strong></td>
                                    <td>Targeted exposure to {ticker} specific market segment</td>
                                    <td>Different exposure profile</td>
                                    <td>Alternative approach to same market</td>
                                </tr>
                                <tr>
                                    <td><strong>Why you might choose it</strong></td>
                                    <td>Best when targeted exposure and market segment focus are the top priorities.</td>
                                    <td>Better fit if you want different exposure or fee structure.</td>
                                    <td>Appealing if you want an alternative approach to the same market exposure.</td>
                                </tr>
                                <tr>
                                    <td><strong>Tradeoff</strong></td>
                                    <td>Focused exposure, but narrow market segment.</td>
                                    <td>Different exposure profile, but may have different characteristics.</td>
                                    <td>Very similar to {ticker}, so the decision may come down to fee, preference, or fund sponsor.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <p class="small-text"><em>For the most current yields and expense ratios of these ETFs, please check
                            a reliable financial data provider like <a href="https://etfdb.com/" target="_blank"
                                rel="noopener noreferrer">ETFdb.com</a>, <a href="https://finance.yahoo.com/etfs"
                                target="_blank" rel="noopener noreferrer">Yahoo Finance</a>, or the individual fund
                            sponsor websites:</em></p>
                    <p class="small-text text-center mt-2">
                        <a href="https://www.ssga.com/us/en/individual/etfs" target="_blank" rel="noopener noreferrer" class="external-link mr-3">State Street <i class="fas fa-external-link-alt"></i></a>
                        <a href="https://www.ishares.com" target="_blank" rel="noopener noreferrer" class="external-link mr-3">iShares <i class="fas fa-external-link-alt"></i></a>
                        <a href="https://www.vanguard.com" target="_blank" rel="noopener noreferrer" class="external-link">Vanguard <i class="fas fa-external-link-alt"></i></a>
                    </p>
                </section>
'''

    def create_final_verdict(self, ticker):
        """Create the final-verdict section"""
        return f'''                <section id="final-verdict" class="section-grey">
                    <div class="final-verdict-box">
                        <h2>The Richiest.com Final Verdict: Is {ticker} Right For You?</h2>
                        <p>If your priority is targeted exposure to a specific market segment, {ticker} delivers focused access with transparency and efficiency. It's liquid, cost-effective, and easy to understand.</p>
                        <p>If your priority is broad market diversification, this may be the wrong tool. {ticker} is best treated as a focused exposure sleeve, not a core holding.</p>
                    </div>
                </section>
'''

    def create_disclaimer(self):
        """Create the disclaimer section"""
        return '''                <section id="disclaimer" class="small-text-section section-grey">
                    <h2>Important Disclaimer</h2>
                    <p>This article is for informational purposes only and does not constitute financial advice.
                        Investing
                        involves risks, and you should consult with a qualified financial professional before making any
                        investment decisions. Past performance is not indicative of future results.</p>
                </section>
'''

    def reformat_file(self, filepath):
        """Reformat a single ETF file to have exactly 10 sections"""
        filepath = Path(filepath)
        if not filepath.exists():
            print(f"  X File not found: {filepath}")
            return False
        
        ticker = self.get_ticker_from_filename(filepath)
        self.ticker = ticker
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata
        title = self.extract_title(content)
        name = self.extract_etf_name(content)
        sub = self.extract_etf_sub(content)
        eyebrow = self.extract_etf_eyebrow(content)
        
        # Create the new HTML structure with CSS
        new_content = f'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{sub}">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <link rel="stylesheet" href="/styles/richiest-etf.css?v=2">
    <style>
        .summary-box {{
            border-left: none;
        }}

        .trust-box {{
            display: flex;
            gap: 16px;
            align-items: flex-start;
            padding: 18px;
            background: #ffffff;
            border: 1px solid #e4e7ec;
            border-radius: 12px;
            margin-bottom: 18px;
        }}

        .trust-box .author-image {{
            margin-top: 0;
            margin-bottom: 0;
            width: 72px;
            min-width: 72px;
            height: 72px;
        }}

        .trust-meta,
        .author-cred,
        .page-note,
        .methodology-note,
        .page-disclosure {{
            font-family: 'DM Sans', sans-serif;
            font-size: 0.95rem;
            line-height: 1.6;
            color: #667085;
            padding-left: 0;
            padding-right: 0;
        }}

        .trust-links {{
            padding: 4px 0 0;
        }}

        .trust-links a {{
            font-family: 'DM Sans', sans-serif;
            font-weight: 500;
        }}

        .methodology-box {{
            background: #ffffff;
            border: 1px solid #e4e7ec;
            border-radius: 12px;
            padding: 18px;
            margin: 18px 0 24px;
        }}

        .page-disclosure {{
            margin-top: 10px;
            padding-left: 10px;
            padding-right: 10px;
        }}

        .pros-cons-table {{
            width: 100%;
        }}

        .pros-cons-table th {{
            width: 50%;
        }}

        .pros-cons-table td {{
            vertical-align: top;
        }}

        .pros-cons-table i {{
            margin-right: 8px;
        }}

        .green-check {{
            color: #28a745;
        }}

        .red-x {{
            color: #dc3545;
        }}

        .chart-container {{
            margin: 24px 0;
        }}

        .chart-container h4 {{
            margin-bottom: 16px;
        }}

        .chart {{
            width: 100%;
            min-height: 400px;
        }}

        .etf-comparison-table {{
            width: 100%;
            margin-top: 24px;
        }}

        .etf-comparison-table th {{
            text-align: center;
        }}

        .etf-comparison-table td {{
            vertical-align: top;
        }}

        .external-link {{
            color: #007bff;
            text-decoration: none;
        }}

        .external-link:hover {{
            text-decoration: underline;
        }}

        .final-verdict-box {{
            background: #ffffff;
            border: 1px solid #e4e7ec;
            border-radius: 12px;
            padding: 24px;
            margin: 24px 0;
        }}

        .small-text-section {{
            font-size: 0.9rem;
        }}

        .persona-box {{
            background: #f8f9fa;
            border-left: 4px solid #007bff;
            padding: 16px;
            margin: 16px 0;
        }}

        .persona-box h3 {{
            margin-top: 0;
        }}

        .table-container {{
            overflow-x: auto;
        }}

        .etf-table {{
            width: 100%;
        }}

        .etf-table th, .etf-table td {{
            padding: 12px;
            vertical-align: top;
        }}

        .small-text {{
            font-size: 0.85rem;
            color: #666;
        }}

        .w-50 {{ width: 50%; }}
        .w-12 {{ width: 12%; }}
        .text-center {{ text-align: center; }}
        .mt-2 {{ margin-top: 8px; }}
        .mb-2 {{ margin-bottom: 8px; }}
        .mr-3 {{ margin-right: 12px; }}
        .mobile-indicator {{
            display: none;
        }}

        @media (max-width: 768px) {{
            .trust-box {{
                flex-direction: column;
            }}
            .trust-box .author-image {{
                width: 60px;
                height: 60px;
            }}
        }}
    </style>
</head>

<body>
    <div class="container-fluid">
        <button id="toggle-toc" class="btn button-fixed-bottom toc-button">TOC</button>
        <button id="return-to-top" class="btn button-fixed-bottom up-arrow"><i class="fas fa-chevron-up"></i></button>
        <div class="container fixed-toc" id="toc-list">
            <div class="etf-nav"></div>
        </div>
        <div class="row sticky-top">
            <div class="col">
                <div class="row bg-white border-bottom border-dark">
                    <div class="col container-1280">
                        <div class="shared-nav"></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="etf-title-header">
            <div class="container container-1000">
                <p class="etf-hero-eyebrow">{eyebrow}</p>
                <h1 class="etf-hero-h1">{name}</h1>
                <p class="etf-hero-sub">{sub}</p>
            </div>
        </div>
        <div class="row">
            <div class="col container-1000">
                <section class="section-white" style="padding-top: 16px; padding-bottom: 16px;">
                    <div class="trust-box">
                        <img src="{self.author_image_url}"
                            alt="Michael Ashley" class="author-image rounded">
                        <div>
                            <span class="author-name">By <a href="/about.html">Michael Ashley</a></span>
                            <p class="author-cred">Banking and asset-management professional with 20+ years of experience across retail banking, commercial banking, investment banking, and performance reporting.</p>
                            <p class="trust-meta"><strong>Last updated:</strong> March 25, 2026</p>
                        </div>
                    </div>
                </section>

{self.create_bottom_line(ticker, name, sub)}
{self.create_overview(ticker, name, sub)}
{self.create_pros_cons(ticker)}
{self.create_who_should_buy(ticker)}
{self.create_price(ticker)}
{self.create_technical_details(ticker, name)}
{self.create_chart(ticker)}
{self.create_comparison(ticker)}
{self.create_final_verdict(ticker)}

            </div>
        </div>
        <div class="row dark-div">
            <div class="col container-1000">
                <div class="shared-subscribe"></div>
            </div>
        </div>
        <div class="row">
            <div class="col container-1000">
{self.create_disclaimer()}
            </div>
        </div>
        <div class="row dark-div">
            <div class="col container-1280">
                <div class="shared-footer"> </div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script>
        function generateTOC() {{
            const tocList = $('#toc-list .etf-nav');
            tocList.empty();
            let ul = $('<ul></ul>').addClass('toc-menu');

            const mainContentArea = $('.container-1000');

            mainContentArea.find('section').each(function () {{
                const sectionId = $(this).attr('id');
                const h2 = $(this).find('h2:first');

                if (sectionId && h2.length > 0 && sectionId !== 'disclaimer') {{
                    let title = h2.text();
                    const li = $('<li></li>');
                    const a = $('<a></a>').attr('href', '#' + sectionId).text(title);
                    li.append(a);
                    ul.append(li);
                }}
            }});
            tocList.append(ul);
        }}

        $(function () {{
            $(".shared-nav").load("/shared/nav.html", function () {{
                generateTOC();
            }});
            $(".shared-subscribe").load("/shared/subscribe.html");
            $(".shared-banner").load("/shared/banner.html");
            $(".shared-articles").load("/shared/technologyStocks.html");
            $(".shared-footer").load("/shared/footer.html");

            generateTOC();

            $("#toggle-toc").click(function () {{
                var fixedToc = $(".fixed-toc");
                fixedToc.toggle();
                if (fixedToc.is(":visible")) {{
                    fixedToc.addClass("show");
                }} else {{
                    fixedToc.removeClass("show");
                }}
            }});

            var mybutton = $('#return-to-top');

            $(window).scroll(function () {{
                if ($(this).scrollTop() > 100) {{
                    mybutton.fadeIn();
                }} else {{
                    mybutton.fadeOut();
                }}
            }});

            mybutton.click(function () {{
                $('html, body').animate({{ scrollTop: 0 }}, 'slow');
                return false;
            }});
        }});
    </script>
</body>

</html>
'''
        
        # Write the reformatted content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  OK: {filepath}")
        return True

    def process_all_files(self, file_list):
        """Process all files in the list"""
        success_count = 0
        fail_count = 0
        
        for filepath in file_list:
            print(f"Processing: {filepath}")
            if self.reformat_file(filepath):
                success_count += 1
            else:
                fail_count += 1
        
        return success_count, fail_count


def main():
    etf_dir = sys.argv[1] if len(sys.argv) > 1 else "/Users/michael/Documents/GitHub/richiest/etfs"
    reformatter = ETFReformatter(etf_dir)
    
    # Define files to process
    index_files = [
        "etfs/index/ddm.html",
        "etfs/index/eps.html",
        "etfs/index/fdn.html",
        "etfs/index/itot.html",
        "etfs/index/ivv.html",
        "etfs/index/qqq.html",
        "etfs/index/qqqm.html",
        "etfs/index/qqqn.html",
        "etfs/index/schb.html",
        "etfs/index/swppx.html",
        "etfs/index/voo.html",
        "etfs/index/vti.html",
    ]
    
    dividend_files = [
        "etfs/dividend/agg.html",
        "etfs/dividend/cgdv.html",
        "etfs/dividend/cowz.html",
        "etfs/dividend/ddm.html",
        "etfs/dividend/des.html",
        "etfs/dividend/dgro.html",
        "etfs/dividend/dgrw.html",
        "etfs/dividend/divo.html",
        "etfs/dividend/dln.html",
        "etfs/dividend/don.html",
        "etfs/dividend/dvy.html",
        "etfs/dividend/fcfy.html",
        "etfs/dividend/fdl.html",
        "etfs/dividend/fthi.html",
        "etfs/dividend/ftqi.html",
        "etfs/dividend/fvd.html",
        "etfs/dividend/hdv.html",
        "etfs/dividend/idvo.html",
        "etfs/dividend/ivv.html",
        "etfs/dividend/ivy.html",
        "etfs/dividend/iwm.html",
        "etfs/dividend/jepi.html",
        "etfs/dividend/jepq.html",
        "etfs/dividend/kng.html",
        "etfs/dividend/kngs.html",
        "etfs/dividend/nobl.html",
        "etfs/dividend/pbp.html",
        "etfs/dividend/pey.html",
        "etfs/dividend/qqew.html",
        "etfs/dividend/qqq.html",
        "etfs/dividend/qqqm.html",
        "etfs/dividend/qqqn.html",
        "etfs/dividend/qyld.html",
        "etfs/dividend/rdvy.html",
        "etfs/dividend/ryld.html",
        "etfs/dividend/schd.html",
        "etfs/dividend/sdy.html",
        "etfs/dividend/sphd.html",
        "etfs/dividend/spyd.html",
        "etfs/dividend/svol.html",
        "etfs/dividend/test.html",
        "etfs/dividend/tltw.html",
        "etfs/dividend/uwm.html",
        "etfs/dividend/vdy.html",
        "etfs/dividend/vig.html",
        "etfs/dividend/vigi.html",
        "etfs/dividend/voo.html",
        "etfs/dividend/vti.html",
        "etfs/dividend/vtwo.html",
        "etfs/dividend/vym.html",
        "etfs/dividend/vymi.html",
        "etfs/dividend/xyld.html",
    ]
    
    all_files = [os.path.join(etf_dir, f) for f in index_files + dividend_files]
    
    print(f"Processing {len(all_files)} ETF files...")
    print("=" * 50)
    
    success, failures = reformatter.process_all_files(all_files)
    
    print("=" * 50)
    print(f"Success: {success} files")
    print(f"Failed: {failures} files")
    
    if failures > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
