from Bio import Entrez
from Bio import SeqIO
import pandas as pd
import sys
import time

##Get Accession numbers from Excel Spreadsheet using python(note I added a column name to the Excel Spreadsheet)##
df = pd.read_excel(sys.argv[1])#read the Excel spreadsheet into the Python module Pandas
uids = df.Accession_ID.to_list()#this command puts the Excel column of accessions into a Python list; assumes accession in are in first excel sheet column

##Now I will obtain the Genbank file for each accession##
timestr = time.strftime("%Y%m%d-%H%M%S")# append the date and time as a string to file name so nothing gets written over
gb_outfile_name = 'fungi_ncbi_data_' + timestr + '.gb'# a generic name I came up with for the Genbank files it grabs
gb_outfile = open(gb_outfile_name, 'w')# open a blank file to store genbank flat files retrieved
Entrez.email = str(sys.argv[2])# I think you have to give your email to pull from the NCBI server
for x in uids:# loop through to list of accessions and grab each one
    fetch_handle = Entrez.efetch(db="nucleotide", id=x, rettype="gb", retmode="text")# the command to search Genbank for the id
    data = fetch_handle.read()# store the Genbank file in computer memory 
    fetch_handle.close()# close Genbank search
    gb_outfile.write(data)# write Genbank records to one concatentated gb file
gb_outfile.close()# close the file I wrote all the Genbank files to

##Loop through each Genbank file and grab the wanted data##
tsv_outfile_name = gb_outfile_name.replace('.gb', '.tsv')# name the tsv outfile the same as the Genbank file, but change the suffix
tsv_outfile = open(tsv_outfile_name, 'w')# open a blank file to store metadata from gb files
header = 'Accession_number\tStrain\tHost\tCountry\tAuthors\tPaper_title\tJournal\n'# column headers for the data parsed from GB files
tsv_outfile.write(header)# write the header to the file
# Lines 29-54: loop through each GB file and get the wanted info from GB features; not elegantly written
with open(gb_outfile_name) as handle:
    for record in SeqIO.parse(handle, "gb"):
        accession_number = record.id
        for feature in record.features:
            if feature.type == "source":
                qual_keys = [x for x in feature.qualifiers.keys()]
                if 'strain' in qual_keys:
                    strain_id = feature.qualifiers['strain'][0]
                elif 'isolate' in qual_keys:
                    strain_id = feature.qualifiers['isolate'][0]
                elif 'clone' in qual_keys:
                    strain_id = feature.qualifiers['clone'][0]
                elif 'specimen_voucher' in qual_keys:
                    strain_id = feature.qualifiers['specimen_voucher'][0]
                else:
                    strain_id = 'NA'
                if 'host' in qual_keys:
                    host_name = feature.qualifiers['host'][0]
                elif 'isolation_source' in qual_keys:
                    host_name = feature.qualifiers['isolation_source'][0]
                else:
                    host_name = 'NA'
                if 'country' in qual_keys:
                    country_name = feature.qualifiers['country'][0]
                else:
                    country_name = 'NA'
# Lines 56-59: getting the 1st pub listed, which is the most recent
        ref = record.annotations['references'][0]
        auths = ref.authors
        paper_title = ref.title
        pub_journal = ref.journal
# Taking all the GB data and putting it in a string and writing it to a line in tsv
        wanted_line = '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (accession_number, strain_id, host_name, country_name, auths, paper_title, pub_journal)
        tsv_outfile.write(wanted_line)
tsv_outfile.close()