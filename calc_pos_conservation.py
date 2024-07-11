### Boas Pucker ###
### b.pucker@tu-bs.de ###
### v0.1 ###

__usage__ = """
					python3 calc_pos_conservation.py
					--in <INPUT_ALIGNMENT_FILE>
					--ref <REF_SEQ_NAME>
					--out <OUTPUT_FILE>
					"""

import os, sys

# --- end of imports --- #


def load_sequences( fasta_file ):
	"""! @brief load sequences of given FASTA file into dictionary with sequence IDs as keys and sequences as values """
	
	sequences = {}
	with open( fasta_file ) as f:
		header = f.readline()[1:].strip()
		seq = []
		line = f.readline()
		while line:
			if line[0] == '>':
					sequences.update( { header: "".join( seq ) } )
					header = line.strip()[1:]
					seq = []
			else:
				seq.append( line.strip() )
			line = f.readline()
		sequences.update( { header: "".join( seq ) } )	
	return sequences


def main( arguments ):
	"""! @brief run generation of plots """
	
	alignment_input_file = arguments[ arguments.index('--in')+1 ]
	ref_seq_name = arguments[ arguments.index('--ref')+1 ]
	output_file = arguments[ arguments.index('--out')+1 ]
	
	sequences = load_sequences( alignment_input_file )
	try:
		ref_seq = sequences[ ref_seq_name ]
	except KeyError:
		sys.exit( "ERROR: reference sequence name not found" )
	
	conservation = []
	seq_names = sequences.keys()
	with open( output_file, "w" ) as out:
		for idx, aa in enumerate( ref_seq ):
			if aa != "-":
				amino_acids = []
				for name in seq_names:
					amino_acids.append( sequences[ name ][ idx ] )
				conservation.append( amino_acids.count( aa ) / len( seq_names ) )
				out.write( aa + "\t" + str( amino_acids.count( aa ) / len( seq_names ) ) + "\n" )


if '--in' in sys.argv and '--ref' in sys.argv and '--out' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
