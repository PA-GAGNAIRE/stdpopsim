import stdpopsim

from . import genome_data

_overall_rate = 1e-8
_recombination_rate = {
    "chr1": _overall_rate,
    "chr2": _overall_rate,
    "chr3": _overall_rate,
    "chr4": _overall_rate,
    "chr5": _overall_rate,
    "chr6": _overall_rate,
    "chr7": _overall_rate,
    "chr8": _overall_rate,
    "chr9": _overall_rate,
    "chr10": _overall_rate,
    "chr11": _overall_rate,
    "chr12": _overall_rate,
    "chr13": _overall_rate,
    "chr14": _overall_rate,
    "chr15": _overall_rate,
    "chr16": _overall_rate,
    "chr17": _overall_rate,
    "chr18": _overall_rate,
    "chr19": _overall_rate,
    "chr20": _overall_rate,
}

_mutation_rate = {
    "chr1": _overall_rate,
    "chr2": _overall_rate,
    "chr3": _overall_rate,
    "chr4": _overall_rate,
    "chr5": _overall_rate,
    "chr6": _overall_rate,
    "chr7": _overall_rate,
    "chr8": _overall_rate,
    "chr9": _overall_rate,
    "chr10": _overall_rate,
    "chr11": _overall_rate,
    "chr12": _overall_rate,
    "chr13": _overall_rate,
    "chr14": _overall_rate,
    "chr15": _overall_rate,
    "chr16": _overall_rate,
    "chr17": _overall_rate,
    "chr18": _overall_rate,
    "chr19": _overall_rate,
    "chr20": _overall_rate,  
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    citations=[],
)
stdpopsim.utils.append_common_synonyms(_genome)

_species = stdpopsim.Species(
    id="GenSpe",
    ensembl_id="genus_species",
    name="Genus species",
    common_name="Genus species",
    genome=_genome,
    generation_time=1,
    population_size=2.5e4,
    citations=[],
)

stdpopsim.register_species(_species)
