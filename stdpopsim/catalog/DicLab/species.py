import stdpopsim

from . import genome_data

_overall_rec = 8.45e-9
_recombination_rate = {
    "LG1A": _overall_rec,
    "LG1B": _overall_rec,
    "LG2": _overall_rec,
    "LG3": _overall_rec,
    "LG4": _overall_rec,
    "LG5": _overall_rec,
    "LG6": _overall_rec,
    "LG7": _overall_rec,
    "LG8": _overall_rec,
    "LG9": _overall_rec,
    "LG10": _overall_rec,
    "LG11": _overall_rec,
    "LG12": _overall_rec,
    "LG13": _overall_rec,
    "LG14": _overall_rec,
    "LG15": _overall_rec,
    "LG16": _overall_rec,
    "LG17": _overall_rec,
    "LG18-21": _overall_rec,
    "LG19": _overall_rec,
    "LG20": _overall_rec,
    "LG22-25": _overall_rec,
    "LG24": _overall_rec,
    "LGx": _overall_rec,
}

_overall_mut = 1e-8
_mutation_rate = {
    "LG1A": _overall_mut,
    "LG1B": _overall_mut,
    "LG2": _overall_mut,
    "LG3": _overall_mut,
    "LG4": _overall_mut,
    "LG5": _overall_mut,
    "LG6": _overall_mut,
    "LG7": _overall_mut,
    "LG8": _overall_mut,
    "LG9": _overall_mut,
    "LG10": _overall_mut,
    "LG11": _overall_mut,
    "LG12": _overall_mut,
    "LG13": _overall_mut,
    "LG14": _overall_mut,
    "LG15": _overall_mut,
    "LG16": _overall_mut,
    "LG17": _overall_mut,
    "LG18-21": _overall_mut,
    "LG19": _overall_mut,
    "LG20": _overall_mut,
    "LG22-25": _overall_mut,
    "LG24": _overall_mut,
    "LGx": _overall_mut,   
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
    population_size=1e5,
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
