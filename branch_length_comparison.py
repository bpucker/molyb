### Boas Pucker ###
### b.pucker@tu-bs.de ###
__version__ = "v0.1"

__reference__ = "TBA"

__usage__ = """
					branch_length_comparison """ + __version__ + """("""+ __reference__ +""")
					
					Usage:
					python3 branch_length_comparison.py
					--tree <TREE_INPUT_FILE>
					--groups <GROUP_INPUT_FILE>
					--out <OUTPUT_DIR>
					
					bug reports and feature requests: b.pucker@tu-bs.de
					"""

import os, glob, sys, dendropy
from scipy import stats

# --- end of imports --- #

def load_groups( group_input_file ):
	"""! @brief load groups """
	
	groups = {}
	with open( group_input_file, "r" ) as f:
		line = f.readline()
		while line:
			parts = line.strip().split('\t')
			if len( parts ) == 2:
				try:
					groups[ parts[1] ].append( parts[0].replace( "_", " " ) )
				except KeyError:
					groups.update( { parts[1]: [ parts[0].replace( "_", " " ) ] } )
			line = f.readline()
	return groups


def main( arguments ):
	"""! @brief run everything """
	
	tree_input_file = arguments[ arguments.index('--tree')+1 ]
	group_input_file = arguments[ arguments.index('--groups')+1 ]
	output_folder = arguments[ arguments.index('--out')+1 ]
	
	# loading groups from input file
	groups = load_groups( group_input_file )
	
	# loading tree from input file
	tree = dendropy.Tree.get( path=tree_input_file, schema="newick" )
	pdm = tree.phylogenetic_distance_matrix()
	#print(pdm.mean_pairwise_distance())
	
	
	# calculate pair-wise distances in tree
	results = {}
	for key in list( groups.keys() ):
		group = groups[ key ]
		intra_group_distances = []
		for idx1, taxon1 in enumerate( group ):
			for idx2, taxon2 in enumerate( group ):
				if idx2 > idx1:
					taxon_obj1 = tree.taxon_namespace.get_taxon( taxon1 )
					#print( taxon_obj1 )
					taxon_obj2 = tree.taxon_namespace.get_taxon( taxon2 )
					#print( taxon_obj2 )
					distance = pdm.patristic_distance( taxon_obj1, taxon_obj2 )
					intra_group_distances.append( distance )
					
		results.update( { key: intra_group_distances } )
	
	# summarize results
	all_keys = list( results.keys() )
	for i1, key1 in enumerate( all_keys ):
		values1 = results[ key1 ]
		if len( values1 ) > 0:
			average = sum( values1 ) / len( values1 )
		else:
			average = None
		#print( values1 )
		print( key1 + ": " + str( average ) )
		
		for i2, key2 in enumerate( all_keys ):
			if i2 > i1:
				values2 = results[ key2 ]
				u, p = stats.mannwhitneyu( values1, values2 )
				print( "Mann-Whitney U statistic (" + key1 + " vs. " + key2 + "): " + str( u ) + "    p-value: " + str( p ) )


if '--tree' in sys.argv and '--out' in sys.argv and '--groups' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
