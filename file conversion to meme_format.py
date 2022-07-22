file = open("/home/bhavana/Desktop/Project_/All_work/agg_fimo_res/Aggregated_conv.txt","r+")
file1 = open("/home/bhavana/Desktop/Project_/All_work/agg_fimo_res/Aggregated_conv_1.txt","w")
for count, i in enumerate(file):
    file1.writelines(">myseq{}\t{}".format(count, i))
file.close()
file1.close()
