"""Trendsplain Daily 2026-11-20: story content. One entry in LINES = one spoken line = one scene.

Each line: (story_key, spoken, headline, card)
 headline: '*word*' is the accent-coloured word.
 card: ("txt", big, small) | ("num", to, prefix, suffix, decimals, small) | ("title", big, small)
Spoken text: numbers as words, hard names respelled for the voice (see sources.md for the real spellings).
"""

ACCENTS = {"intro": "#FF4A4F", "summit": "#FF4A4F", "icj": "#5CC8FF", "quad": "#FFD23F", "tara": "#FF9F1C",
           "mahanadi": "#2EC4B6", "akvan": "#5CC8FF", "uproll": "#C77DFF", "ladakh": "#2EC4B6",
           "maha": "#FFD23F", "khet": "#2EC4B6", "q1": "#C77DFF", "q2": "#2EC4B6", "q3": "#FF4A4F",
           "q4": "#5CC8FF", "outro": "#FF4A4F"}

STORIES = [  # key, label, icon, source line
    ("intro", "TRENDSPLAIN DAILY", "globe", "Trendsplain Daily · 20 November 2026"),
    ("summit", "WORLD · 1 OF 10", "globe", "Source: ABC News, Moscow Times, Daily Sabah · 19 Nov 2026"),
    ("icj", "WORLD · 2 OF 10", "gavel", "Source: Radio Free Asia, Jerusalem Post, The Hill · 19 Nov 2026"),
    ("quad", "INDIA · 3 OF 10", "handshake", "Source: Al Jazeera, PTI via The Week · 17 Nov 2026"),
    ("tara", "INDIA · 4 OF 10", "tanker", "Source: Khaleej Times, Gulf News, News On AIR · 16-18 Nov 2026"),
    ("mahanadi", "INDIA · 5 OF 10", "coal", "Source: Kotak Neo, Angel One · 16 Nov 2026 · Not investment advice"),
    ("akvan", "STATE · 6 OF 10", "cyclone", "Source: IMD forecast via OneIndia, The Federal, Outlook · 16-17 Nov 2026"),
    ("uproll", "STATE · 7 OF 10", "ballot", "Source: PTI via OneIndia, News24 · 17 Nov 2026"),
    ("ladakh", "STATE · 8 OF 10", "mountain", "Source: News On AIR, Daily Pioneer, GKToday · 10-11 Nov 2026"),
    ("maha", "VILLAGE · 9 OF 10", "drought", "Source: Deccan Chronicle, ANI via Republic · 15-17 Oct 2026"),
    ("khet", "VILLAGE · 10 OF 10", "field", "Source: News On AIR, UNI · 17 Nov 2026"),
    ("q1", "QUICK HIT · SPACE", "probe", "Source: EarthSky, ABC News · 17-18 Nov 2026"),
    ("q2", "QUICK HIT · INDIA", "solar", "Source: Amazon, ESG Today, YourStory · 17 Nov 2026"),
    ("q3", "QUICK HIT · WORLD", "gavel", "Source: AP via ABC News, Korea Times · 19 Nov 2026"),
    ("q4", "QUICK HIT · WORLD", "drops", "Source: 1News, Xinhua, PINA · 18 Nov 2026"),
    ("outro", "SEE YOU TOMORROW", "globe", "Sources are listed in the description"),
]

LINES = [
    # ---------------- intro
    ("intro", "Before you scroll today, here are the fourteen stories that matter, from the world to your village, in plain words.",
     "TODAY'S *14* STORIES", ("title", "20 NOV", "Trendsplain Daily · world to village")),
    ("intro", "Ten stories in depth first, then four quick hits. Let's begin.",
     "10 IN DEPTH · *4* QUICK", ("txt", "10 + 4", "in depth, then quick hits")),

    # ---------------- 1 summit
    ("summit", "Story one. The leaders of the United States, China and Russia met together in Shun Jen, China, on Thursday.",
     "THREE LEADERS, *ONE* ROOM", ("txt", "US · CHINA · RUSSIA", "Shenzhen, China · Thursday 19 Nov")),
    ("summit", "It was the first sit down of the three. President Trump met Xi and Putin one on one first, then all three talked for a little over an hour.",
     "THE FIRST *SIT-DOWN*", ("num", 1, "", "+ hour", 0, "all three together, after one-on-one talks")),
    ("summit", "They released a four point peace declaration. It covers United Nations reform, oil supply, lowering nuclear risk, and a warning that international courts must not abuse their power.",
     "A FOUR-POINT *DECLARATION*", ("txt", "UN REFORM · OIL · NUCLEAR RISK · COURTS", "the four points")),
    ("summit", "It did not mention the war in Ukraine, or the war with Iran.",
     "NOT *MENTIONED*", ("txt", "UKRAINE · IRAN", "left out of the declaration")),
    ("summit", "Who is affected? Ukraine did not take part. Nor did Germany, France, Britain, Japan or South Korea.",
     "WHO WAS *ABSENT*", ("txt", "UKRAINE NOT IN THE ROOM", "no European or Asian allies took part")),
    ("summit", "Why it matters: the United States and Russia each have more than five thousand nuclear warheads, and China has more than six hundred. The leaders said a nuclear war should never be fought, but they announced no cuts.",
     "WHY IT *MATTERS*", ("num", 5000, "", "+", 0, "warheads each: US and Russia · China 600+")),
    ("summit", "What happens next? They agreed to start a dialogue on reducing nuclear risks. Mister Trump said he will hold a news conference at the White House on Friday.",
     "WHAT *NEXT*", ("txt", "NUCLEAR-RISK DIALOGUE", "Trump news conference: Friday")),

    # ---------------- 2 icj
    ("icj", "Story two. The top United Nations court has ruled that Myanmar committed genocide against the Ro hin ja people.",
     "COURT SAYS *GENOCIDE*", ("txt", "MYANMAR · ROHINGYA", "International Court of Justice, The Hague")),
    ("icj", "The International Court of Justice gave its ruling on Thursday, by nine votes to six.",
     "THE VOTE", ("txt", "9 – 6", "judges, ruling on Thursday 19 Nov")),
    ("icj", "The judges said soldiers, police and border guards killed around ten thousand Ro hin ja civilians in two thousand seventeen.",
     "AROUND *10,000* KILLED", ("num", 10000, "~", "", 0, "Rohingya civilians killed in 2017, per the ruling")),
    ("icj", "Hundreds of thousands fled to Bangladesh. About one point two million Ro hin ja still live in camps there.",
     "STILL IN *CAMPS*", ("num", 1.2, "", " million", 1, "Rohingya in Bangladesh camps")),
    ("icj", "The case was brought in twenty nineteen by a small country, The Gambia. Myanmar says its operations were a response to attacks by a militant group.",
     "BROUGHT BY *THE GAMBIA*", ("txt", "FILED IN 2019", "Myanmar says it answered militant attacks")),
    ("icj", "Why it matters: this is the first time this court has found a state responsible for genocide.",
     "A *FIRST*", ("txt", "FIRST STATE FOUND RESPONSIBLE", "by this court")),
    ("icj", "What happens next? The court ordered Myanmar to stop ongoing violations, investigate suspects and give restitution. Myanmar has two years to report back.",
     "WHAT *NEXT*", ("num", 2, "", " years", 0, "for Myanmar to report back")),

    # ---------------- 3 quad
    ("quad", "Story three. The leaders of the Quad met in Manila, in the Philippines, on Tuesday.",
     "QUAD MEETS IN *MANILA*", ("txt", "INDIA · US · AUSTRALIA · JAPAN", "Tuesday 17 Nov, Philippines")),
    ("quad", "The Quad is a group of four countries. Prime Minister Modi, President Trump, Prime Minister Albanese and Prime Minister Ta kai chi took part.",
     "WHO *ATTENDED*", ("txt", "MODI · TRUMP · ALBANESE · TAKAICHI", "leaders of the four countries")),
    ("quad", "It was their first summit in two years. The last one was in Wilmington, in the United States, in twenty twenty four.",
     "FIRST IN *2 YEARS*", ("num", 2, "", " years", 0, "since the last summit, Wilmington 2024")),
    ("quad", "Mister Modi called the Quad a constructive and trusted partnership, covering sea safety, supply chains, new technology and disaster response.",
     "A *TRUSTED* PARTNERSHIP", ("txt", "SEA SAFETY · SUPPLY CHAINS · TECH", "areas Modi named")),
    ("quad", "Mister Trump said the group is launching a Quad A I accelerator, with more than eighty five million dollars to help countries in the Indo Pacific use trusted A I.",
     "QUAD *AI* ACCELERATOR", ("num", 85, "$", " million+", 0, "to expand access to trusted AI")),
    ("quad", "He also announced deals to secure critical minerals, so that no single supplier can use them as pressure. He did not name China.",
     "CRITICAL *MINERALS*", ("txt", "NO SINGLE SUPPLIER", "China was not named")),
    ("quad", "What happens next? A first Quad Business Leaders Forum will be held, and more new projects will be announced next year.",
     "WHAT *NEXT*", ("txt", "BUSINESS LEADERS FORUM", "more projects announced next year")),

    # ---------------- 4 tara gas
    ("tara", "Story four. A gas tanker with Indian sailors on board was attacked in the Strait of Hor mooz on Monday, the sixteenth of November.",
     "TANKER HIT IN *HORMUZ*", ("txt", "MT TARA GAS", "attacked Monday 16 Nov")),
    ("tara", "The ship is called Tara Gas. It carries cooking gas, L P G, and flies the flag of Panama.",
     "THE SHIP", ("txt", "PANAMA-FLAGGED LPG TANKER", "carries cooking gas")),
    ("tara", "Twenty four Indians were on board. Twenty one were taken ashore safely at Khasab, in Oman. Two are injured in hospital. One is missing.",
     "24 INDIANS *ON BOARD*", ("num", 24, "", " on board", 0, "21 ashore · 2 injured · 1 missing")),
    ("tara", "India's foreign ministry condemned the attack. It said attacks on commercial ships must end and free sailing must be restored.",
     "INDIA *CONDEMNS*", ("txt", "ATTACKS MUST END", "India's foreign ministry")),
    ("tara", "Why it matters: this is the second attack in a week on a tanker with Indian sailors. On the eleventh, another tanker was hit off the United Arab Emirates, and all twenty two crew were rescued.",
     "SECOND ATTACK IN *A WEEK*", ("num", 2, "", " attacks", 0, "11 Nov: 22 crew rescued · 16 Nov: Tara Gas")),
    ("tara", "The strait carried about one fifth of the world's crude oil before the conflict with Iran.",
     "A *KEY* SEA LANE", ("txt", "~1/5 OF WORLD CRUDE", "passed through before the Iran conflict")),
    ("tara", "What happens next? The Indian embassy in Oman is working with Omani authorities to search for the missing sailor.",
     "WHAT *NEXT*", ("txt", "SEARCH FOR 1 MISSING SAILOR", "Indian embassy in Oman, with Oman")),

    # ---------------- 5 mahanadi
    ("mahanadi", "Story five. A big coal company is selling shares to the public for the first time. It is called Mahanadi Coalfields.",
     "COAL *IPO* OPEN", ("txt", "MAHANADI COALFIELDS", "bidding 19 to 23 Nov")),
    ("mahanadi", "An I P O, or initial public offer, is when a company sells its shares to the public so it can be listed on the stock exchange.",
     "WHAT IS AN *IPO*", ("txt", "SHARES SOLD TO THE PUBLIC", "to list on the stock exchange")),
    ("mahanadi", "Mahanadi is fully owned by Coal India. It runs seventeen mines in Odisha, fourteen open pit and three underground.",
     "17 MINES IN *ODISHA*", ("num", 17, "", " mines", 0, "14 open pit · 3 underground")),
    ("mahanadi", "The price band is one hundred and twenty nine to one hundred and thirty six rupees a share. The issue is worth about eight thousand nine hundred and eighty one crore rupees. A crore is ten million.",
     "THE *PRICE* BAND", ("txt", "₹129 – ₹136 A SHARE", "issue size about ₹8,981 crore")),
    ("mahanadi", "All the shares are being sold by Coal India. So the company itself gets no money from this sale.",
     "ALL SHARES *FOR SALE*", ("txt", "SOLD BY COAL INDIA", "the company gets no proceeds")),
    ("mahanadi", "In the last financial year, the company's profit after tax was about ten thousand six hundred and ninety eight crore rupees, down one percent.",
     "LAST YEAR'S *PROFIT*", ("num", 10698, "₹", " crore", 0, "profit after tax, FY26 · down 1%")),
    ("mahanadi", "Bidding closes on the twenty third of November. Listing is expected on the twenty seventh. This is not investment advice.",
     "NOT *INVESTMENT ADVICE*", ("txt", "CLOSES 23 NOV · LISTING 27 NOV", "this is not investment advice")),

    # ---------------- 6 akvan
    ("akvan", "Story six. Cyclone Ack van is heading for the coast of Andhra Pradesh. The weather department expects it to cross the coast on Friday, the twentieth, around noon.",
     "CYCLONE *AKVAN* NEARS", ("txt", "ANDHRA PRADESH COAST", "forecast landfall: Fri 20 Nov, ~noon")),
    ("akvan", "It is expected to cross between Nell ore and Too nee, as a very severe cyclonic storm.",
     "BETWEEN *NELLORE* AND TUNI", ("txt", "VERY SEVERE CYCLONIC STORM", "IMD forecast")),
    ("akvan", "Winds of one hundred and twenty to one hundred and thirty kilometres an hour are expected, with gusts up to one hundred and forty five.",
     "WINDS OF *145* KM/H", ("num", 145, "", " km/h", 0, "gusts · sustained 120 to 130")),
    ("akvan", "Extremely heavy rain, more than twenty one centimetres in a day, is forecast for north coastal Andhra on the nineteenth and twentieth.",
     "EXTREMELY *HEAVY* RAIN", ("num", 21, "", "+ cm", 0, "in a day, north coastal Andhra")),
    ("akvan", "Who is affected? Coastal Andhra Pradesh, south Odisha and Tamil Nadu. Fishermen have been asked not to go to sea, and Odisha has begun moving people from vulnerable areas.",
     "WHO IS *AFFECTED*", ("txt", "ANDHRA · ODISHA · TAMIL NADU", "fishermen told to stay ashore")),
    ("akvan", "Why it matters: this is the third cyclone in under a month. Andhra Pradesh says two earlier storms have already caused losses of more than seven thousand crore rupees.",
     "THIRD CYCLONE IN *A MONTH*", ("num", 7000, "₹", " crore+", 0, "losses from two earlier storms, per Andhra")),
    ("akvan", "What happens next? Officials will track the storm as it crosses the coast. Rain is also forecast for Odisha on the twenty first.",
     "WHAT *NEXT*", ("txt", "ODISHA RAIN: 21 NOV", "track the IMD bulletins")),

    # ---------------- 7 up roll
    ("uproll", "Story seven. Uttar Pradesh has published its draft list of voters, ahead of the state assembly election in twenty twenty seven.",
     "UP'S *DRAFT* VOTER LIST", ("txt", "UTTAR PRADESH", "published Tuesday 17 Nov")),
    ("uproll", "The list has thirteen point five eight crore voters. That is about eighteen point eight four lakh more than in April. A lakh is one hundred thousand.",
     "13.58 CRORE *VOTERS*", ("num", 13.58, "", " crore", 2, "voters on the draft list")),
    ("uproll", "There are seven point three eight crore men, six point two zero crore women, and four thousand and forty two voters of the third gender.",
     "MEN, WOMEN, *THIRD GENDER*", ("txt", "7.38 CR · 6.20 CR · 4,042", "men · women · third gender")),
    ("uproll", "Eleven point eight three lakh voters are aged eighteen to nineteen.",
     "YOUNGEST *VOTERS*", ("num", 11.83, "", " lakh", 2, "voters aged 18 to 19")),
    ("uproll", "Why it matters: the election officer says about sixteen crore people in the state are eighteen or older, based on population estimates. So the list is about two point five eight crore short of that estimate.",
     "A *GAP* OF 2.58 CRORE", ("txt", "~16.16 CR ADULTS (ESTIMATE)", "vs 13.58 crore on the list")),
    ("uproll", "What happens next? People can file claims and objections from the seventeenth of November to the sixteenth of December. Special camps run on the twenty first, twenty second, twenty eighth and twenty ninth of November. The final list comes out on the fourth of January.",
     "WHAT *NEXT*", ("txt", "FINAL LIST: 4 JANUARY", "claims open until 16 Dec")),

    # ---------------- 8 ladakh
    ("ladakh", "Story eight. Ladakh will vote on the fourth of December to elect its hill development councils.",
     "LADAKH *VOTES* 4 DEC", ("txt", "HILL DEVELOPMENT COUNCILS", "polling Friday 4 December")),
    ("ladakh", "Newly set up councils will cover all eight districts of Ladakh, with one hundred seats in all.",
     "100 SEATS, *8* DISTRICTS", ("num", 100, "", " seats", 0, "across eight districts")),
    ("ladakh", "Thirty six of the hundred seats are reserved for women, for the first time.",
     "36 SEATS FOR *WOMEN*", ("num", 36, "", " seats", 0, "reserved for women, a first")),
    ("ladakh", "Nominations closed on the seventeenth. Today, the twentieth, is the last day to withdraw.",
     "TODAY: LAST DAY TO *WITHDRAW*", ("txt", "NOMINATIONS CLOSED 17 NOV", "withdrawal deadline: 20 Nov")),
    ("ladakh", "Not everyone agrees. Earlier this month Kargil saw a full shutdown, called by the Kargil Democratic Alliance, over timing and how seats were drawn. In Leh, the Apex Body asked to delay the vote to April or May because of winter snow.",
     "NOT *EVERYONE* AGREES", ("txt", "KARGIL SHUTDOWN · LEH ASKS TO DELAY", "timing, seat drawing, winter snow")),
    ("ladakh", "What happens next? Voting is on the fourth of December, and the whole process is to finish by the eighth.",
     "WHAT *NEXT*", ("txt", "PROCESS ENDS 8 DEC", "voting 4 Dec")),

    # ---------------- 9 maharashtra drought
    ("maha", "Story nine. In Maharashtra, farmers hit by drought are getting an advance payment of five thousand rupees each.",
     "₹5,000 FOR *DROUGHT* FARMERS", ("num", 5000, "₹", "", 0, "advance per farmer, Maharashtra")),
    ("maha", "Chief Minister Devendra Fadnavis announced it on the fourteenth of October, before Diwali. Drought has been declared in around three hundred talukas.",
     "AROUND *300* TALUKAS", ("num", 300, "~", " talukas", 0, "declared drought-hit")),
    ("maha", "The government estimated the cost at six thousand crore rupees, reaching about one crore ten lakh to one crore twenty lakh farmers.",
     "THE *COST*", ("num", 6000, "₹", " crore", 0, "estimated cost · 1.1 to 1.2 crore farmers")),
    ("maha", "Mister Fadnavis called it unprecedented, and said it cannot cover all losses. Each eligible farmer gets at least five thousand rupees now, and the rest is paid later.",
     "AN *ADVANCE*, NOT THE FULL SUM", ("txt", "THE REST COMES LATER", "Fadnavis: it cannot cover all losses")),
    ("maha", "Opposition parties and farmers have criticised the amount as too small. A loan waiver for another three and a half lakh farmers is also to begin.",
     "CRITICS *SAY* TOO SMALL", ("txt", "LOAN WAIVER: 3.5 LAKH MORE FARMERS", "opposition and farmers criticised the amount")),
    ("maha", "What happens next? The reports we checked, from October, do not say whether every farmer has been paid yet.",
     "WHAT *NEXT*", ("txt", "PAYMENT STATUS NOT CONFIRMED", "reports checked are from October")),

    # ---------------- 10 khet bachao
    ("khet", "Story ten. The Union government has approved more than three hundred and fifty crore rupees for farming in Punjab.",
     "₹350 CRORE FOR *PUNJAB*", ("num", 352.64, "₹", " crore", 2, "254.20 + 98.44 crore approved")),
    ("khet", "Agriculture Minister Shivraj Singh Chouhan handed over the approval letters at Badarpur village, in Mo ha lee district, on Tuesday, the seventeenth.",
     "AT *BADARPUR* VILLAGE", ("txt", "MOHALI DISTRICT, PUNJAB", "Tuesday 17 Nov")),
    ("khet", "Two hundred and fifty four point two zero crore rupees is for this year under a scheme called P M R K V Y. Ninety eight point four four crore is for seven new projects.",
     "TWO *APPROVALS*", ("txt", "₹254.20 CR · ₹98.44 CR", "PM-RKVY 2026-27 · 7 new projects")),
    ("khet", "The event was part of the Khet Bachao Abhiyan, or Save the Field campaign. Mister Chouhan spoke about crop residue and new farming technology.",
     "SAVE THE *FIELD*", ("txt", "KHET BACHAO ABHIYAN", "crop residue · new technology")),
    ("khet", "Green ammonia, made with solar power, is being tried in place of urea on ten thousand hectares across the country, including one thousand and eight hectares in Punjab.",
     "GREEN *AMMONIA* TRIAL", ("num", 10000, "", " hectares", 0, "trial across India · 1,008 ha in Punjab")),
    ("khet", "Mister Chouhan said the only aim is to improve the lives of the farmers of Punjab.",
     "THE *AIM*", ("txt", "BETTER LIVES FOR PUNJAB'S FARMERS", "Shivraj Singh Chouhan")),

    # ---------------- quick hits
    ("q1", "Quick hit one. Voyager One, launched in nineteen seventy seven, reached one light day from Earth on the eighteenth of November. A radio signal now takes a full day to reach it.",
     "VOYAGER 1: *ONE LIGHT-DAY*", ("num", 25.9, "", " billion km", 1, "from Earth · launched 1977")),
    ("q1", "It is about twenty five point nine billion kilometres away, the farthest any human made object has gone.",
     "THE *FARTHEST*", ("txt", "FARTHEST HUMAN-MADE OBJECT", "still sending signals")),
    ("q2", "Quick hit two. Amazon says it will invest seven billion dollars more in renewable energy in India by two thousand thirty, on top of four billion dollars already contracted.",
     "AMAZON: *$7 BILLION* MORE", ("num", 7, "$", " billion", 0, "by 2030, plus $4 billion contracted")),
    ("q2", "Four new projects add up to nine hundred and thirty four megawatts, in Karnataka, Madhya Pradesh and Rajasthan.",
     "934 *MEGAWATTS*", ("num", 934, "", " MW", 0, "Karnataka · Madhya Pradesh · Rajasthan")),
    ("q3", "Quick hit three. South Korea's top court on Thursday overturned the conviction of former prime minister Han Dook soo for helping with the martial law order of December twenty twenty four.",
     "HAN DUCK-SOO *OVERTURNED*", ("txt", "SOUTH KOREA'S TOP COURT", "ex-prime minister · martial law case")),
    ("q3", "His fifteen year sentence was overturned, and the case now goes back to the Seoul High Court.",
     "BACK TO *SEOUL HIGH COURT*", ("num", 15, "", "-year term", 0, "overturned · case sent back")),
    ("q4", "Quick hit four. Fiji has declared a nationwide state of disaster because of a drought linked to El Nino. It lasts up to thirty days and can be extended.",
     "FIJI: STATE OF *DISASTER*", ("num", 30, "up to ", " days", 0, "can be extended by Cabinet")),
    ("q4", "More than two million litres of emergency water were delivered to island communities in the past month.",
     "WATER *DELIVERIES*", ("num", 2, "", " million litres+", 0, "emergency water, past month")),

    # ---------------- outro
    ("outro", "That was Trendsplain Daily for the twentieth of November. Every source is listed in the description. Subscribe, and we will see you tomorrow.",
     "SEE YOU *TOMORROW*", ("title", "TRENDSPLAIN", "subscribe · new video every day")),
]

if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w").write("\n".join(l[1] for l in LINES) + "\n")
    print(len(LINES), "lines,", sum(len(l[1].split()) for l in LINES), "words")
