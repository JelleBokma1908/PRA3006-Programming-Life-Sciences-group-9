import csv

def csv_to_ttl(csv_file, ttl_file):
    
    with open(csv_file, mode='r') as infile:
        reader = csv.DictReader(infile)

        
        with open(ttl_file, mode='w') as outfile:
            outfile.write('@prefix myData: <http://example.org/myData/> .\n\n')

            i =0
            for row in reader:
                i += 1
                species = row['Species']
                gene_name = row['Gene name']
                brain_region = row['Brain region']
                tpm = row['TPM']
                print(i)

                
                outfile.write(f'<http://example.org/myData/species/{species}> rdf:type myData:Species ;\n')
                outfile.write(f'    myData:speciesName "{species}" ;\n') 
                outfile.write(f'    myData:hasGene <http://example.org/myData/species/{species}/gene/{gene_name}> .\n\n')
                outfile.write(f'<http://example.org/myData/species/{species}/gene/{gene_name}> rdf:type myData:Gene ;\n')
                outfile.write(f'    myData:geneName "{gene_name}" ;\n')
                tpmIRI = f"<http://example.org/myData/species/{species}/gene/{gene_name}/tpm/t{tpm}>";
                outfile.write(f'    myData:hasTPM {tpmIRI} .\n\n')
                outfile.write(f'{tpmIRI} rdf:type myData:GeneTPM ;\n')
                outfile.write(f'    myData:hasValue "{tpm}"^^xsd:float ;\n')
                outfile.write(f'    myData:locatedIn <http://example.org/myData/species/{species}/region/{brain_region}> .\n\n')
                outfile.write(f'<http://example.org/myData/species/{species}/region/{brain_region}> rdf:type myData:BrainRegion ;\n')
                outfile.write(f'    myData:regionName "{brain_region}" .\n\n')


csv_file = 'TPM_human_and_mouse_dataset_excel.csv'  
ttl_file = 'TPM_human_and_mouse_dataset_turtle.ttl'  

csv_to_ttl(csv_file, ttl_file)

