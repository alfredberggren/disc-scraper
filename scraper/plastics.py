import re

PLASTICS = {
    "latitude-64/frost",
    "dynamic-discs/fuzion",
    "latitude-64/opto-ice",
    "discraft/pro-d",
    "millennium/quantum-lunar-glow",
    "innova/dx-glow",
    "quest/premier",
    "dga/sp-line",
    "kastaplast/",
    "dga/",
    "westside/vip-air",
    "prodigy/400g-glow",
    "prodigy/750-glow",
    "clash-discs/hard",
    "prodigy/400-tie-dye",
    "viking/armor",
    "alfa-discs/crystal",
    "legacy/icon",
    "latitude-64/zero-hybrid-moonshine",
    "gateway/pro-line",
    "clash-discs/hardy",
    "/",
    "streamline-discs/streamline-electron",
    "discraft/esp",
    "westside/vip",
    "prodigy/400g",
    "loeft-discs-loft/alpha-solid",
    "Snap/egr",
    "gateway/organic",
    "discraft/",
    "quest/standard",
    "westside/tournament-decodye",
    "launch-discs/noble-glow",
    "launch-discs/omega",
    "rip-disc-golf/grip-plastic",
    "millennium/quantum",
    "latitude-64/sense",
    "legacy/pinnacle",
    "dynamic-discs/fuzion-dyemax-marvel",
    "discwing/shockline™",
    "discmania/blizzard-c-line",
    "prodigy/basegrip-glow",
    "ledig/recycled-launch",
    "discraft/elite-z",
    "skyquest-discs/recycled-premium",
    "dynamic-discs/classic",
    "prodigy/300-glow",
    "discraft/photon-glo",
    "dynamic-discs/prime",
    "kastaplast/k1-line",
    "gateway/superglow",
    "millennium/sirius",
    "westside/bt",
    "millenium/quantum",
    "dynamic-discs/fluid-moonshine",
    "prodigy/750",
    "prodigy/duraflex-glow",
    "momentum/flex",
    "discraft/z",
    "westside/hybrid-ws",
    "innova/champion-i-dye",
    "discmania/exo",
    "discmania/x-line",
    "dynamic-discs/",
    "launch-discs/alpha",
    "gateway/pure-white",
    "innova/xt",
    "latitude-64/gold-dyemax",
    "prodigy/400",
    "prodiscus/ultrium",
    "discmania/vapor",
    "discmania/glow-c-line",
    "discmania/forge",
    "kastaplast/k1-x-out",
    "millennium/m-line",
    "gateway/nylon-rubber-alloy",
    "westside/vip-x",
    "hyzer-bombs/frontline",
    "infinite-discs/",
    "discmania/active-premium-glow",
    "latitude-64/opto-x",
    "mvp-disc-sports/r2-neutron",
    "latitude-64/gold-x-blend",
    "daredevil/hp",
    "discmania/c-line",
    "galaxy-discs/e-class",
    "prodigy/400-air",
    "discraft/titanium",
    "mvp-disc-sports/neutron",
    "dynamic-discs/fuzion-x-blend",
    "latitude-64/gold-ice",
    "discmania/s-line",
    "legacy/gravity",
    "dga/midnight-flyer",
    "innova/star",
    "latitude-64/gold",
    "latitude-64/recycled",
    "discraft/z-lite",
    "millenium/sirius",
    "alfa-discs/chrome",
    "innova/nexus",
    "prodiscus/premium",
    "mvp-disc-sports/proton",
    "discmania/lux",
    "millennium/delta-t",
    "latitude-64/eze",
    "latitude-64/grip",
    "kastaplast/k1-soft-x-out",
    "dga/rdga-line",
    "lone-star-disc/bravo",
    "prodigy/350g",
    "viking/ground",
    "viking/storm",
    "prodigy/duraflex",
    "westside/elasto-moonshine",
    "discraft/putter-line",
    "discmania/neo",
    "dynamic-discs/biofuzion",
    "mvp-disc-sports/plasma",
    "innova/star-mix",
    "innova/r-pro",
    "alfa-discs/",
    "discmania/geo",
    "prodigy/proflex",
    "dynamic-discs/lucid",
    "innova/xt-overmold",
    "discmania/active-line",
    "mvp-disc-sports/fission",
    "latitude-64/gold-dyemax-marvel",
    "dynamic-discs/lucid-air",
    "legacy/protégé",
    "discmania/sg-line",
    "discmania/p-line",
    "discmania/",
    "launch-discs/alpha-glow",
    "evolvent-discs/apex-80",
    "millennium/quantum-zero-g",
    "dynamic-discs/fuzion-dyemax",
    "discraft/z-glo",
    "dga/signature-line",
    "momentum/buddy",
    "launch-discs/noble",
    "discmania/horizon",
    "discmania/g-line",
    "prodigy/200",
    "hyzer-bombs/base",
    "innova/gstar",
    "dynamic-discs/hybrid-dd;hybrid;hybrid-moonshine",
    "latitude-64/opto",
    "kastaplast/k1-soft",
    "westside/tournament",
    "lightning/maxline",
    "westside/elasto",
    "westside/vip-moonshine",
    "innova/champion-glow",
    "dga/dga-proline",
    "discmania/active-premium-line",
    "momentum/",
    "kastaplast/k3-line",
    "kastaplast/k1-glow-line",
    "dynamic-discs/lucid-x",
    "innova/champion",
    "westside/origo",
    "streamline-discs/streamline-neutron",
    "discraft/z-fly-dye",
    "millenium/m-line",
    "clash-discs/steady",
    "westside/origio",
    "latitude-64/gold-decodye",
    "innova/",
    "thought-space-athletics/",
    "discmania/exo-lumen",
    "gateway/g-series",
    "prodigy/",
    "launch-discs/safefly",
    "latitude-64/snow",
    "discraft/x",
    "rpm-discs/atomic",
    "kastaplast/k3-x-out",
    "latitude-64/hybrid-64",
    "latitude-64/opto-air",
    "hyzer-bombs/",
    "prodigy/500",
    "millennium/lunar",
    "latitude-64/",
    "latitude-64/2k-line-opto-g",
    "latitude-64/eco",
    "daredevil/fp",
    "vibram/x-link",
    "discwing/baseline",
    "prodigy/basegrip",
    "prodigy/300",
    "prodigy/300-soft",
    "gateway/special-blend",
    "westside/",
    "latitude-64/goldhex",
    "latitude-64/optohex",
    "latitude-64/opto-moonshine",
    "gateway/diamond",
    "discmania/d-line",
    "dynamic-discs/lucid-moonshine",
    "westside/tournament-dyemax-marvel",
    "discraft/esp-supercolor",
    "legacy/excel",
    "innova/pro",
    "prodigy/350",
    "mvp-disc-sports/eclipse",
    "innova/dx",
    "latitude-64/zero-hybrid",
    "latitude-64/frost-moonshine",
    "westside/eco1",
    "ev-7/",
    "hyzer-bombs/recon",
    "gateway/s-series",
    "westside/tournament-dyemax",
    "prodigy/450",
    "prodiscus/basic",
    "latitude-64/grand",
    "ching/power",
    "Snap/firegrade",
    "dga/d-line",
    "lightning/li-standard-plastic",
    "latitude-64/retro",
    "innova/blizzard-champion",
    "Snap/gummy-egr",
    "discmania/s-line-echo",
    "streamline-discs/streamline-proton",
    "mvp-disc-sports/electron",
    "ching/supreme",
    "latitude-64/zero",
    "discraft/photon-uv",
    "westside/tournament-x-blend",
    "discraft/flx",
    "ev-7/og",
    "discmania/meta",
    "lightning/prostyle",
    "discraft/z-flx",
    "millennium/et",
    "galaxy-discs/c-class",
    "dynamic-discs/fluid",
    "loeft-discs-loft/",
    "hyzer-bombs/frontline-x",
    "aerobie/special-blend",
    "gateway/hyper-diamond",
    "gateway/eraser",
    "kastaplast/k1-glow-x-out",
    "discraft/jawbreaker",
    "prodigy/400-glow",
    "ev-7/basplast",
    "westside/moonshine",
    "discraft/rubber-blend",
    "innova/halo-star;halo",
}


def variations(plastic_str: str):
    """
    Returns variations of a certain plastic name

    For example, Discmanias "S-Line" plastic could be expressed as:
        * S line
        * s-line
        * S
        * and so on...
    """

    parts = plastic_str.split("/")
    manufacturer = parts[0]
    plastic_string = parts[1]
    inh_variations = plastic_string.split(";")
    plastic_name = inh_variations[0]

    if (
        manufacturer is None
        or plastic_name is None
        or len(manufacturer) == 0
        or len(plastic_name) == 0
    ):
        return None

    plastic_variations = set()
    plastic_variations.add(plastic_name)

    for v in inh_variations:
        plastic_variations.add(v)

    if manufacturer.casefold() == "discmania" or manufacturer.casefold() == "kastaplast":
        plastic_variations.update(discmania_variations(plastic_name))

    temp = plastic_variations.copy()
    for var in temp:
        if "-" in var:
            plastic_variations.add(var.replace("-", " "))

    return plastic_variations


def discmania_variations(plastic_name: str):
    """
    Discmania usually puts "line" after their plastics name.
    This method removes this variation to match on sites that doesn't use this particular notation for various reasons
    """
    variations = set()

    if "line" not in plastic_name:
        variations.add(f"{plastic_name}-line")
    else:
        # TODO: what if 's-line-echo' for example
        variations.add(re.search("(.*)-line", plastic_name).group(1))

    return variations
