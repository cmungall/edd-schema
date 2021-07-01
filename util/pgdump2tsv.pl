#!/usr/bin/perl
use Text::ParseWords;
%seed = ();
while(<>) {
    chomp;
    my $db = $ARGV;
    #print STDERR "$db\n" if $db ne 'metadata_plus.jbei.sql';
    $db =~ s@^data/@@;
    if (m@^COPY (\S+)\s+\((.*)\) FROM stdin@) {
        $t = $1;
        @hdr = split(/, /,$2);
        @hdr = (@hdr, "db_instance");
        my @toks = split(/\./, $t);
        $t = $toks[-1];
        if ($seen{$t}) {
            print STDERR "Appending to $t\n";
            open(F, ">>tmp/$t.tsv");
        }
        else {
            print STDERR "Writing to $t\n";
            open(F, ">tmp/$t.tsv");
            $seen{$t}++;
        }
            
        print F join("\t", @hdr)."\n";;
        while(<>) {
            chomp;
            if (m@^\\\.@) {
                last;
            }
            @vals = split(/\t/);
            @vals = map {fix($_)} @vals;
            if (!$db) {
                die $_;
            }
            @vals = (@vals, $db);
            print F join("\t", @vals)."\n";
        }
        close(F)
    }
}
exit 0;

sub fix {
    $_ = $_[0];
    if (m@^\\N@) {
        return '';
    }
    if (m@^\{(.*)\}@) {
        my @f = quotewords ',', 0, $1;
        return join('|',@f);
    }
    return $_;
        
}
