from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an English vocabulary assistant. Use \"-\" to list text. Please explain me the meaning of the words I'll provide you following this template: # Word: {{provided English word}} ({{word translated to Portuguese}})  \n## Meaning(s)  \n### As a {{List the meanings according to the possibles part of speech}}  \n## Usage Examples  \n{{At least 3 usage examples}}## synonyms  \n",
        ),
        ("user", "{text}"),
    ]
)

chain = prompt_template | model | parser

words = ["abolish", "abortion", "absence", "absent", "absurd", "abuse", "academy", "accelerate", "acceptance", "accessible", "accomplishment", "accordingly", "accountability", "accountable", "accumulate", "accumulation", "accusation", "accused", "acid", "acquisition", "activation", "activist", "acute", "adaptation", "adhere", "adjacent", "adjustment", "administer", "administrative", "administrator", "admission", "adolescent", "adoption", "adverse", "advocate", "aesthetic", "affection", "aftermath", "aggression", "agricultural", "aide", "alert", "align", "alignment", "alike", "allegation", "allege", "allegedly", "alliance", "allocate", "allocation", "allowance", "ally", "aluminum", "amateur", "ambassador", "amend", "amendment", "amid", "analogy", "anchor", "angel", "anonymous", "apparatus", "apparel", "appealing", "appetite", "applaud", "applicable", "appoint", "appreciation", "arbitrary", "architectural", "archive", "arena", "arm (verb)", "array", "articulate", "ash", "aspiration", "aspire", "assassination", "assault", "assemble", "assembly", "assert", "assertion", "assurance", "asylum", "atrocity", "attain", "attendance", "attribute", "auction", "audit", "authentic", "authorize", "auto", "autonomy", "autumn", "availability", "await"]

c1_word_map = {
"a": ["abolish", "abortion", "absence", "absent", "absurd", "abuse", "academy", "accelerate", "acceptance", "accessible", "accomplishment", "accordingly", "accountability", "accountable", "accumulate", "accumulation", "accusation", "accused", "acid", "acquisition", "activation", "activist", "acute", "adaptation", "adhere", "adjacent", "adjustment", "administer", "administrative", "administrator", "admission", "adolescent", "adoption", "adverse", "advocate", "aesthetic", "affection", "aftermath", "aggression", "agricultural", "aide", "alert", "align", "alignment", "alike", "allegation", "allege", "allegedly", "alliance", "allocate", "allocation", "allowance", "ally", "aluminum", "amateur", "ambassador", "amend", "amendment", "amid", "analogy", "anchor", "angel", "anonymous", "apparatus", "apparel", "appealing", "appetite", "applaud", "applicable", "appoint", "appreciation", "arbitrary", "architectural", "archive", "arena", "arm (verb)", "array", "articulate", "ash", "aspiration", "aspire", "assassination", "assault", "assemble", "assembly", "assert", "assertion", "assurance", "asylum", "atrocity", "attain", "attendance", "attribute", "auction", "audit", "authentic", "authorize", "auto", "autonomy", "autumn", "availability", "await"],
"b": ["backdrop", "backing", "backup", "bail", "ballot", "bankruptcy", "banner", "bare", "barrel", "bass", "battlefield", "bay", "beam", "beast", "behalf", "behavioral", "beloved", "bench", "benchmark", "beneath", "beneficiary", "betray", "beverage", "bind", "biography", "bishop", "bizarre", "blade", "blast", "bleed", "blend", "bless", "blessing", "boast", "bonus", "booking", "boom", "bounce", "boundary", "bow", "breach", "breakdown", "breakthrough", "breed", "broadband", "browser", "brutal", "buddy", "buffer", "bulk", "burden", "bureaucracy", "burial", "burst"],
"c": ["cabinet", "calculation", "canvas", "capability", "capitalism", "capitalist", "cargo", "carriage", "carve", "casino", "casualty", "catalog", "cater", "cattle", "caution", "cautious", "cease", "cemetery", "chamber", "chaos", "characterise", "charm", "charter", "choir", "chronic", "chunk", "circulate", "circulation", "citizenship", "civic", "civilian", "clarity", "clash", "classification", "cling", "clinical", "closure", "cluster", "coalition", "coastal", "cocktail", "cognitive", "coincide", "collaborate", "collaboration", "collective", "collision", "colonial", "columnist", "combat", "commence", "commentary", "commentator", "commerce", "commissioner", "commodity", "communist", "companion", "comparable", "compassion", "compel", "compelling", "compensate", "compensation", "competence", "competent", "compile", "complement", "complexity", "compliance", "complication", "comply", "composition", "compromise", "compute", "conceal", "concede", "conceive", "conception", "concession", "condemn", "confer", "confession", "configuration", "confine", "confirmation", "confront", "confrontation", "congratulate", "congregation", "congressional", "conquer", "conscience", "consciousness", "consecutive", "consensus", "consent", "conserve", "consistency", "consolidate", "constitute", "constitution", "constitutional", "constraint", "consultation", "contemplate", "contempt", "contend", "contender", "content", "contention", "continually", "contractor", "contradiction", "contrary", "contributor", "conversion", "convict", "conviction", "cooperate", "cooperative", "coordinate", "coordination", "coordinator", "copper", "copyright", "correction", "correlate", "correlation", "correspond", "correspondence", "correspondent", "corresponding", "corrupt", "corruption", "costly", "councilor", "counseling", "counselor", "counter (argue)", "counterpart", "countless", "coup", "courtesy", "craft", "crawl", "creator", "credibility", "credible", "creep", "critique", "crown", "crude", "crush", "crystal", "cult", "cultivate", "curiosity", "custody", "cutting", "cynical"],
"d": ["dam", "damaging", "dawn", "debris", "debut", "decision-making", "decisive", "declaration", "dedicated", "dedication", "deed", "deem", "default", "defect", "defensive", "deficiency", "deficit", "defy", "delegate", "delegation", "delicate", "demon", "denial", "denounce", "dense", "density", "dependence", "depict", "deploy", "deployment", "deprive", "deputy", "descend", "descent", "designate", "desirable", "desktop", "destructive", "detain", "detection", "detention", "deteriorate", "devastate", "devil", "devise", "diagnose", "diagnosis", "dictate", "dictator", "differentiate", "dignity", "dilemma", "dimension", "diminish", "dip", "diplomat", "diplomatic", "directory", "disastrous", "discard", "discharge", "disclose", "disclosure", "discourse", "discretion", "discrimination", "dismissal", "displace", "disposal", "dispose", "dispute", "disrupt", "disruption", "dissolve", "distinction", "distinctive", "distort", "distress", "disturbing", "divert", "divine", "doctrine", "documentation", "domain", "dominance", "donor", "dose", "drain", "drift", "driving", "drown", "dual", "dub", "dumb", "duo"],
"e": ["earnings", "ease", "echo", "ecological", "educator", "effectiveness", "efficiency", "ego", "elaborate", "electoral", "elevate", "eligible", "elite", "embark", "embarrassment", "embassy", "embed", "embody", "emergence", "empirical", "empower", "enact", "encompass", "encouragement", "encouraging", "endeavor", "endless", "endorse", "endorsement", "endure", "enforce", "enforcement", "engagement", "engaging", "enrich", "enroll", "ensue", "enterprise", "enthusiast", "entitle", "entity", "epidemic", "equality", "equation", "erect", "escalate", "essence", "establishment", "eternal", "evacuate", "evoke", "evolutionary", "exaggerate", "excellence", "exceptional", "excess", "exclusion", "exclusive", "exclusively", "execute", "execution", "exert", "exile", "expenditure", "experimental", "expire", "explicit", "explicitly", "exploitation", "explosive", "extremist"],
"f": ["facilitate", "faction", "fade", "fairness", "fatal", "fate", "favorable", "feat", "felony", "feminist", "fiber", "fierce", "filmmaker", "filter", "fine", "firearm", "fiscal", "fit", "flaw", "flawed", "flee", "fleet", "flesh", "flexibility", "flourish", "fluid", "footage", "foreigner", "forge", "formula", "formulate", "forth", "forthcoming", "foster", "fragile", "franchise", "frankly", "freshman", "frustrated", "frustrating", "frustration", "functional", "fundraising", "funeral"],
"g": ["gambling", "gathering", "gaze", "gear", "generic", "genocide", "gig", "glance", "glimpse", "glorious", "glory", "governance", "grace", "grasp", "grave (cemetery)", "grave (serious)", "gravity", "grid", "grief", "grin", "grind", "grip", "gross", "guerrilla", "guidance", "guilt", "gut"],
"h": ["hail", "halfway", "halt", "handful", "handling", "handy", "harassment", "hardware", "harmony", "harsh", "harvest", "hatred", "haunt", "hazard", "heighten", "heritage", "hierarchy", "high-profile", "hint", "homeland", "hopeful", "horizon", "horn", "hostage", "hostile", "hostility", "humanitarian", "humanity", "humble", "hydrogen"],
"i": ["identification", "ideological", "ideology", "idiot", "ignorance", "imagery", "immense", "imminent", "implementation", "imprison", "inability", "inadequate", "inappropriate", "incarcerate", "incarceration", "incidence", "inclined", "inclusion", "incur", "indicator", "indictment", "indigenous", "induce", "indulge", "inequality", "infamous", "infant", "infect", "inflict", "influential", "inherent", "inhibit", "initiate", "inject", "injection", "injustice", "inmate", "inquire", "insertion", "insider", "inspect", "inspection", "inspiration", "instinct", "institutional", "instruct", "instrumental", "insufficient", "insult", "intact", "intake", "integral", "integrated", "integration", "integrity", "intensify", "intensity", "intensive", "intent", "interactive", "interface", "interfere", "interference", "interim", "interior", "intermediate", "intersection", "intervene", "intervention", "intimate", "intriguing", "inventory", "investigator", "invisible", "invoke", "involvement", "ironic", "ironically", "irony", "irrelevant", "isolation"],
"j": ["judicial", "jurisdiction", "just", "justification"],
"k": ["keen", "kidnap", "kidney", "kingdom"],
"l": ["landlord", "landmark", "lap", "large-scale", "laser", "latter", "lawmaker", "lawn", "lawsuit", "layout", "leak", "leap", "legacy", "legendary", "legislation", "legislative", "legislature", "legitimate", "lengthy", "lesbian", "lesser", "lethal", "liable", "liberal", "liberation", "liberty", "lifelong", "likelihood", "limb", "linear", "lineup", "linger", "listing", "liter", "literacy", "liver", "lobby", "log", "logic", "long-standing", "longtime", "loom", "loop", "loyalty"],
"m": ["machinery", "magical", "magnetic", "magnitude", "mainland", "mainstream", "maintenance", "mandate", "mandatory", "manifest", "manipulate", "manipulation", "manuscript", "march", "marginal", "marine", "marketplace", "mask", "massacre", "mathematical", "mature", "maximize", "meaningful", "meantime", "medieval", "meditation", "melody", "memo", "memoir", "memorial", "mentor", "merchant", "mercy", "mere", "merely", "merge", "merger", "merit", "methodology", "midst", "migration", "militant", "militia", "mill", "minimal", "minimize", "mining", "ministry", "minute", "miracle", "misery", "misleading", "missile", "mob", "mobile", "mobility", "mobilize", "moderate", "modification", "module", "momentum", "monk", "monopoly", "morality", "motive", "municipal", "mutual"],
"n": ["namely", "nationwide", "naval", "neglect", "neighboring", "nest", "net", "newsletter", "niche", "noble", "nod", "nominate", "nomination", "nominee", "nonetheless", "nonprofit", "nonsense", "noon", "notable", "notably", "notify", "notorious", "novel", "nursery"],
"o": ["objection", "oblige", "obsess", "obsession", "occasional", "occurrence", "odds", "offering", "offspring", "operational", "opt", "optical", "optimism", "oral", "organisational", "orientation", "originate", "outbreak", "outing", "outlet", "outlook", "outrage", "outsider", "overlook", "overly", "oversee", "overturn", "overwhelm", "overwhelming"],
"p": ["pad", "parameter", "parental", "parliament", "partial", "partially", "passing", "passive", "pastor", "patent", "pathway", "patrol", "patron", "peak", "peasant", "peculiar", "pension", "persist", "persistent", "personnel", "petition", "philosopher", "philosophical", "pioneer", "pipeline", "pirate", "pit", "plea", "plead", "pledge", "plug", "plunge", "pole", "poll", "pond", "pop", "portfolio", "portray", "postpone", "postwar", "practitioner", "preach", "precedent", "precision", "predator", "predecessor", "predominantly", "pregnancy", "prejudice", "preliminary", "premier", "premise", "premium", "prescribe", "prescription", "presently", "preservation", "preside", "presidency", "prestigious", "presumably", "presume", "prevail", "prevalence", "prevention", "prey", "privatization", "privilege", "probe", "problematic", "proceeding", "proceeds", "processing", "processor", "proclaim", "productive", "productivity", "profitable", "profound", "projection", "prominent", "pronounced", "propaganda", "proposition", "prosecute", "prosecution", "prosecutor", "prospective", "prosperity", "protective", "protocol", "province", "provincial", "provision", "provoke", "psychiatric", "pulse", "pump", "punch"],
"q": ["query", "quest", "quota"],
"r": ["radar", "radical", "rage", "raid", "rally", "ranking", "rape", "ratio", "rational", "ray", "readily", "realization", "realm", "rear", "reasoning", "reassure", "rebel", "rebellion", "recipient", "reconstruction", "recount", "recruitment", "referendum", "reflection", "reform", "refuge", "refusal", "regain", "regardless", "regime", "regulator", "regulatory", "rehabilitation", "reign", "rejection", "relevance", "reliability", "reluctant", "remainder", "remains", "remedy", "reminder", "removal", "render", "renew", "renowned", "rental", "replacement", "reportedly", "representation", "reproduce", "reproduction", "republic", "resemble", "reside", "residence", "residential", "residue", "resignation", "resistance", "respective", "respectively", "restoration", "restraint", "resume", "retreat", "retrieve", "revelation", "revenge", "reverse", "revival", "revive", "revolutionary", "rhetoric", "rifle", "riot", "rip", "ritual", "robust", "rock", "rod", "rookie", "roster", "rotate", "rotation", "ruling", "rumour"],
"s": ["sacred", "sacrifice", "saint", "sake", "sanction", "say", "scattered", "scope", "screw", "scrutiny", "seal", "secondly", "secular", "seemingly", "segment", "seize", "seldom", "selective", "sensation", "sensitivity", "sentiment", "separation", "serial", "settlement", "setup", "sexuality", "shareholder", "shatter", "shed", "sheer", "shipping", "shoot", "shrink", "shrug", "sigh", "simulate", "simulation", "simultaneously", "sin", "situated", "skeptical", "sketch", "skip", "slam", "slap", "slash", "slavery", "slot", "smash", "snap", "soak", "soar", "socialist", "sole", "solely", "solidarity", "solo", "sophomore", "sound", "sovereignty", "spam", "span", "spark", "specialized", "specification", "specimen", "spectacle", "spectrum", "spell", "sphere", "spin", "spine", "spotlight", "spouse", "spy", "squad", "squeeze", "stab", "stability", "stabilize", "stake", "standing", "stark", "statistical", "steer", "stem", "stereotype", "stimulus", "stir", "storage", "straightforward", "strain", "strand", "strategic", "strip (narrow piece)", "strive", "structural", "stumble", "stun v.", "submission", "subscriber", "subscription", "subsidy", "substantial", "substantially", "substitute", "substitution", "subtle", "suburban", "succession", "successive", "successor", "suck", "sue", "suicide", "suite", "summit", "superb", "superintendent", "superior", "supervise", "supervision", "supervisor", "supplement", "supportive", "supposedly", "suppress", "supreme", "surge", "surgical", "surplus", "surrender", "surveillance", "suspension", "suspicion", "suspicious", "sustain", "swing", "sword", "symbolic", "syndrome", "synthesis", "systematic"],
"t": ["tackle", "tactic", "tactical", "taxpayer", "tempt", "tenant", "tender", "tenure", "terminate", "terrain", "terrific", "testify", "testimony", "texture", "thankfully", "theatrical", "theology", "theoretical", "thereafter", "thereby", "thoughtful", "thread", "threshold", "thrilled", "thrive", "tide", "tighten", "timber", "timely", "tobacco", "tolerance", "tolerate", "toll", "top", "torture", "toss", "total", "toxic", "trademark", "trail", "trailer", "transaction", "transcript", "transformation", "transit", "transmission", "transparency", "transparent", "trauma", "treaty", "tremendous", "tribal", "tribute", "trio", "triumph", "trophy", "troubled", "trustee", "tuition", "tumor", "turnout", "turnover", "twist"],
"u": ["unconstitutional", "undergraduate", "underlying", "undermine", "undoubtedly", "unify", "unprecedented", "unveil", "upcoming", "upgrade", "uphold", "utility", "utilize", "utterly"],
"v": ["vacuum", "vague", "validity", "vanish", "variable", "varied", "vein", "venture", "verbal", "verdict", "verify", "verse", "versus", "vessel", "veteran", "viable", "vibrant", "vice", "vicious", "violate", "violation", "virtue", "vocal", "vow", "vulnerability", "vulnerable"],
"w": ["ward", "warehouse", "warfare", "warrant", "warrior", "weaken", "weave", "weed", "well", "well-being", "whatsoever", "whereby", "whip", "wholly", "widen", "widow", "width", "willingness", "wipe", "wit", "withdrawal", "workout", "worship", "worthwhile", "worthy"],
"y": ["yell", "yield"]
}

for current_key, words in c1_word_map.items():
        with open(f"out/c1-wordlist/{current_key}.md", "a") as f:
            for word in words:
                output = chain.invoke({"text": word})
                f.write(f"{output}\n\n")
        print(f"Output saved to {current_key}.md.")
