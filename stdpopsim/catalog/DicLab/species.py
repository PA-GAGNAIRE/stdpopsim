import stdpopsim

from . import genome_data

_recombination_rate = {
    "LG1A": 1e-8,
    "LG1B": 1e-8,
    "LG2": 1e-8,
    "LG3": 1e-8,
    "LG4": 1e-8,
    "LG5": 1e-8,
    "LG6": 1e-8,
    "LG7": 1e-8,
    "LG8": 1e-8,
    "LG9": 1e-8,
    "LG10": 1e-8,
    "LG11": 1e-8,
    "LG12": 1e-8,
    "LG13": 1e-8,
    "LG14": 1e-8,
    "LG15": 1e-8,
    "LG16": 1e-8,
    "LG17": 1e-8,
    "LG18-21": 1e-8,
    "LG19": 1e-8,
    "LG20": 1e-8,
    "LG22-25": 1e-8,
    "LG24": 1e-8,
    "LGx": 1e-8,
}

_overall_rate = 8.45e-9
_mutation_rate = {
    "LG1A": _overall_rate,
    "LG1B": _overall_rate,
    "LG2": _overall_rate,
    "LG3": _overall_rate,
    "LG4": _overall_rate,
    "LG5": _overall_rate,
    "LG6": _overall_rate,
    "LG7": _overall_rate,
    "LG8": _overall_rate,
    "LG9": _overall_rate,
    "LG10": _overall_rate,
    "LG11": _overall_rate,
    "LG12": _overall_rate,
    "LG13": _overall_rate,
    "LG14": _overall_rate,
    "LG15": _overall_rate,
    "LG16": _overall_rate,
    "LG17": _overall_rate,
    "LG18-21": _overall_rate,
    "LG19": _overall_rate,
    "LG20": _overall_rate,
    "LG22-25": _overall_rate,
    "LG24": _overall_rate,
    "LGx": _overall_rate,   
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    citations=[
        stdpopsim.Citation(
            author="Tine et al",
            year=2014,
            doi="https://doi.org/10.1038/ncomms6770"
,
            reasons={stdpopsim.CiteReason.ASSEMBLY, stdpopsim.CiteReason.REC_RATE, stdpopsim.CiteReason.MUT_RATE},
        ),
        stdpopsim.Citation(
            author="Duranton et al",
            year=2018,
            doi="https://doi.org/10.1038/s41467-018-04963-6"
,
            reasons={stdpopsim.CiteReason.POP_SIZE},
        ),
    ],
)
stdpopsim.utils.append_common_synonyms(_genome)

_species = stdpopsim.Species(
    id="DicLab",
    ensembl_id="dicentrarchus_labrax",
    name="Dicentrarchus labrax",
    common_name="Dicentrarchus labrax",
    genome=_genome,
    generation_time=5,
    population_size=100e5,
    citations=[
        stdpopsim.Citation(
            author="Tine et al",
            year=2014,
            doi="https://doi.org/10.1038/ncomms6770"
,
            reasons={stdpopsim.CiteReason.POP_SIZE, stdpopsim.CiteReason.GEN_TIME},
        ),
    ],
)

stdpopsim.register_species(_species)
