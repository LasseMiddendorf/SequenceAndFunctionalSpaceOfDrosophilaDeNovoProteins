#!/home/bharat/julia-stable/bin/julia
using DelimitedFiles
using StatsBase
using HypothesisTests
using MultipleTesting

cd(Base.source_dir())


samples = ["random","denovo","conserved","consrand"]

if length(ARGS) > 2
	@warn "more than two arguments: only using first two"
end

if any(ARGS .∉ Ref(samples))
	@error "argument must be 'random', 'denovo', or 'conserved'"
end

println("Calculating pairwise tests for distances between " * ARGS[1] * " and " * ARGS[2])

function nondiag(mat::Matrix)
	sm = size(mat)
	if(sm[1]!=sm[2])
		@error "Matrix must be square"
	else
		return [mat[i,j] for i=1:size(mat,1),j=1:size(mat,2) if i!=j]
	end
end

sn11 = ARGS[1]*"-"*ARGS[1]
sn12 = ARGS[1]*"-"*ARGS[2]
sn22 = ARGS[2]*"-"*ARGS[2]

d11 = nondiag(readdlm(sn11*"_dist.txt"));
d12 = vcat(readdlm(sn12*"_dist.txt")...);
d22 = nondiag(readdlm(sn22*"_dist.txt"));

function performMWT(xdata,ydata)
	mwt = MannWhitneyUTest(xdata,ydata)
	mx = median(xdata)
	my = median(ydata)
	if(my>mx)
		alt = :left
	else
		alt = :right
	end
	p = pvalue(mwt, tail = alt)
	return [mx  my  p]
end

result = vcat(performMWT(d11,d12), performMWT(d22,d12));
header = ["Sample-1" "Sample-2" "Median-1" "Median-2" "pvalue"];
outdata = vcat(header,hcat([sn11 sn12; sn22 sn12],result))

outfile = sn12*"_distTest.txt"

writedlm(outfile,outdata)