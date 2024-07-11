using StatsPlots
using DelimitedFiles
using Measures
using StatsBase

cd("/home/bharat/Documents/ProteinSeqSpace/")
function nondiag(mat::Matrix)
	sm = size(mat)
	if(sm[1]!=sm[2])
		@error "Matrix must be square"
	else
		return [mat[i,j] for i=1:size(mat,1),j=1:size(mat,2) if i!=j]
	end
end

cm2pt = (cm) -> 28.3465*cm
figdir = joinpath(Base.source_dir(),"../Manuscripts/M3/Figures/");
colors = ["#FFCC00","#5599FF","#D40000","#754473","#000000"];
lstyles = [:solid,:dash,:dot]

default(linecolor = :black, linewidth = 2, tickfont = font(10,"Helvetica"), 
guidefont = font(13,"Helvetica"),framestyle = :box, legend = false);

rr = nondiag(readdlm("random-random_dist.txt"));
dr = vcat(readdlm("denovo-random_dist.txt")...);
dd = nondiag(readdlm("denovo-denovo_dist.txt"));
dc = vcat(readdlm("denovo-conserved_dist.txt")...);
cc = nondiag(readdlm("conserved-conserved_dist.txt"));
rc = vcat(readdlm("random-conserved_dist.txt")...);


alldata = [rr,dr,dd,dc,cc,rc];
plt = plot(ylabel ="L1 Distance",  size = (width = cm2pt(20), height = cm2pt(12)));;

violin!(plt,alldata);
scatter!(plt,[1:6;], median.(alldata), markersize = 7, markercolor = :white);

xticks!(plt,([1:6;],["Random\nRandom","De novo\nRandom","De novo\nDe novo", "De novo\nConserved", "Conserved\nConserved","Random\nConserved"]));

savefig(plt,"Plot_distances.pdf")