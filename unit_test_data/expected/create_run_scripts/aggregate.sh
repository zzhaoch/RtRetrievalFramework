#!/usr/bin/env bash
export spectrum_file="/fake_path/spectrum.h5"

export ecmwf_file="/fake_path/ecmwf.h5"

export imap_file="/fake_path/imap.h5"

sounding_id_list_filename=create_run_scripts_test/sounding_id.list
l2_agg_fn=create_run_scripts_test/l2_aggregate.h5
l2_plus_more_agg_fn=create_run_scripts_test/l2_plus_more_aggregate.h5

export PYTHONPATH=/fake_python_path
export PATH=/fake_bin_path
export LD_LIBRARY_PATH=/fake_lib_path
export LUA_PATH="/fake_path/input/gosat/config/?.lua;/l2_lua_fake_path"

# Aggregate all single sounding output hdf files into a single hdf file
if [ ! -e "$l2_agg_fn" ]; then
    # Use find instead of a glob because there could be too much files that
    # could exhaust the command line length limit
    input_files_tmp=$(mktemp)
    find create_run_scripts_test/output -name "*.h5" > $input_files_tmp

    # Make a version of the sounding id file with newlines instead of spaces
    # for use by splice tool
    in_snd_id_tmp=$(mktemp)
    cat $sounding_id_list_filename | tr ' ' '\n' > $in_snd_id_tmp

    echo "Aggregating L2 output files"
    /l2_support_fake_path/utils/splice_product_files.py -o $l2_agg_fn -i $input_files_tmp -s $in_snd_id_tmp $*

    rm $input_files_tmp
    rm $in_snd_id_tmp
else
    echo "L2 aggregated file exists, skipping creation"
fi

if [ ! -e "$l2_plus_more_agg_fn" ]; then
    echo "Creating L2 plus L1B aggregated file"
    # Extract sounding ids, and reformat into a format that can be used by splice tool
    # Take sounding ids from L2 aggregate so we know which soundings actually completed
    # Otherwise we will have empty values for L2 datasets when we include IMAP or ABO2
    # data.
    l2_snd_id_tmp1=$(mktemp)
    l2_snd_id_tmp2=$(mktemp)
    h5dump --noindex -o $l2_snd_id_tmp1 -d RetrievalHeader/sounding_id_reference $l2_agg_fn > /dev/null

    # This line below, turns commas into new lines, removes empty spaces and blank lines
    cat $l2_snd_id_tmp1 | sed 's|,|\n|g' | sed -r 's|^[ ]*||' | grep -v '^$' > $l2_snd_id_tmp2
    rm $l2_snd_id_tmp1

    # Combine L1B and L2 files into one file
    # with IMAP and ABand files if they are supplied
    echo "Combining L2 and L1B into a single file"
    /l2_support_fake_path/utils/splice_product_files.py --splice-all --rename_mapping --agg_names_filter -o $l2_plus_more_agg_fn $l2_agg_fn $spectrum_file $imap_file $aband_file -s $l2_snd_id_tmp2
    rm $l2_snd_id_tmp2

    # Create retrieval_index dataset based on L1B file
    echo "Adding retrieval information datasets"
    /l2_support_fake_path/utils/add_spliced_retrieval_info.py $spectrum_file $l2_plus_more_agg_fn
else
    echo "L2 plus L1B file exists, skipping creation"
fi

