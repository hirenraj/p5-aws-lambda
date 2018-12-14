#!/usr/local/bin/perl

#==================================================================
# ���́F WwwCount Ver3.16
# ��ҁF �m��X
# �ŐV�œ����F http://tohoho.wakusei.ne.jp/wwwsoft.htm
# ��舵���F �t���[�\�t�g�B���p/����/�Ĕz�z�\�B�m�F���[���s�v�B
# ���쌠�FCopyright (C) 1996-2018 �m��X
#==================================================================

#==================================================================
# �g�������F
#==================================================================
#   (����1) wwwcount.cgi?test
#	CGI���g�p�ł��邩�e�X�g���s���B
#
#   (����2) wwwcount.cgi?text
#	�J�E���g�A�b�v���s���A�J�E���^���e�L�X�g�ŕ\������B
#
#   (����3) wwwcount.cgi?gif
#	�J�E���g�A�b�v���s���A�J�E���^��GIF�ŕ\������B
#
#   (����4) wwwcount.cgi?hide+xxx.gif
#	�J�E���g�A�b�v���s���Axxx.gif��\������B

#==================================================================
# �J�X�^�}�C�Y�F
#==================================================================

# �� ���̃t�@�C���� 1�s�ڂ́u#!/usr/local/bin/perl�v�� perl �̃p�X
#    ���ɂ��킹�ēK�؂ɏ��������Ă��������B�p�X��������Ȃ��ꍇ�́A
#    �v���o�C�_��T�[�o�[�Ǘ��҂ɖ₢���킹�Ă��������B#! �̑O�ɂ�
#    ��s���X�y�[�X����������Ȃ��悤�ɂ��Ă��������B�i�K�{�j

# �� Windows NT �� IIS ���g�p����ꍇ�́Awwwcount.cgi ���C���X�g�[
#    ������Ă���t�H���_���� 'C:/HomePage/cgi-bin' �Ȃǂ̂悤�Ɏw
#    �肵�Ă��������B�i�K�{�j
$chdir = '';

# �� SSI�̃e�L�X�g���[�h�Ŏg�p����ꍇ�́A$mode = "text"; �Ƃ��Ă�
#    �������B�i�K�{�j
$mode = "";

# �� CGI�Ƃ��Ă͓����Ă���̂ɁAwwwcount.cgi?test �Ńe�X�g�ł��Ȃ�
#    �ꍇ�A���L��1�s�̐擪�� # ���폜���Ă݂Ă��������B
#@ARGV = split(/\+/, $ENV{'QUERY_STRING'});

# �� �\��������Ⴆ��5���Ɏw�肷��ꍇ�́u$figure = 5;�v�̂悤�Ɏw
#    �肵�Ă��������B0 ���w�肷��ƌ������������ɂȂ�܂��B
$figure = 6;

# �� �t�@�C�����b�N�@�\���I���ɂ���ꍇ�� 1 ���A�I�t�ɂ���ꍇ�� 0
#    ���w�肵�Ă��������B�ʏ�� 1 �ł悢�ł��傤�B
$do_file_lock = 1;

# �� ���A�h���X�`�F�b�N�@�\���I���ɂ���ꍇ�� 1 ���w�肵�Ă��������B
#    �������ɓ��� IP �A�h���X����̃A�N�Z�X���J�E���g�A�b�v���Ȃ�
#    �Ȃ�܂��B
$do_address_check = 0;

# �� ���|�[�g�@�\���g���ꍇ�́u$mailto = 'abc@xxx.yyy.zzz';�v�̂悤
#    �Ɏ����̃��[���A�h���X��ݒ肵�Ă��������B�T�[�o�[�� sendmail
#    �R�}���h���T�|�[�g����Ă���K�v������܂��B
$mailto  = '';

# �� ���|�[�g�@�\�̑��M�����[���A�h���X�i�ʏ�͎����̃A�h���X�j��
#    �w�肵�Ă��������B�ȗ����̓J�E���^���ɂȂ�܂����A�v���o�C�_
#    �ɂ���ẮA���M�����[���A�h���X���K�؂Ȃ��̂��`�F�b�N���Ă�
#    ��P�[�X������܂��B
$mailfrom = '';

# �� ���|�[�g�@�\�ŁAsendmail �R�}���h�̃p�X���� /usr/lib/sendmail
#    �ƈقȂ�ꍇ�́A�K�؂ɏC�����Ă��������B
$sendmail = '/usr/lib/sendmail';

# �� ���|�[�g�@�\�ŁA�ڍ׏���Y�t�����A�A�N�Z�X�����݂̂����|�[
#    �g����ꍇ�́A0 ���w�肵�Ă��������B
$account_detail = 1;

# �� ���|�[�g�@�\�ŁA�A�N�Z�X���̃z�X�g�����擾�ł��Ȃ��ꍇ�ɁA�́A
#    ���̒l�� 1 �ɕύX����ƁAIP�A�h���X����z�X�g���ւ̕ϊ�������
#    ��悤�ɂȂ�܂��B�z�X�g���ϊ��́A�T�[�o�[���ׂ̌����ɂ��Ȃ��
#    �ł����ӂ��������B
$do_addr_to_host = 0;

# �� ���|�[�g�@�\�ɂ����āA�u$my_url = 'http://www.yyy.zzz/';�v�Ƃ�
#    ��ƁA���̃A�h���X�Ƀ}�b�`����T�C�g����� FROM �͕\�����Ȃ���
#    ��܂��B
$my_url = '';

# �� ���|�[�g�@�\�ŁA%7E �Ȃǂ̃G���R�[�h�������f�R�[�h���ċL�^����
#    �ꍇ�� 1 ���A���̂܂܋L�^����ꍇ�� 0 ���w�肵�Ă��������B
$do_decode_url = 0;

# �� �ȗ����̃J�E���^�[�����w�肵�܂��B�J�E���^�[���� *.cnt �� *.dat
#    �Ȃǂ̃t�@�C�����ɑΉ����Ă��܂��B
$count_name = "wwwcount";

#==================================================================
# �������F
#==================================================================

#
# �J�����g�t�H���_��ύX����B
#
if ($chdir ne "") {
	chdir($chdir);
}

#
# �֘A����t�@�C����􂢏o���Ă���
#
$file_count  = "$count_name" . ".cnt";
$file_date   = "$count_name" . ".dat";
$file_access = "$count_name" . ".acc";
$file_lock   = "lock/$count_name" . ".loc";

#
# ���������߂���
#
@ARGV = split(/\+/, $ENV{'QUERY_STRING'});
for ($i = 0; $i <= $#ARGV; $i++) {
	if ($ARGV[$i] eq "test") {
		test();
	} elsif ($ARGV[$i] eq "text") {
		$mode = "text";
	} elsif ($ARGV[$i] eq "gif") {
		$mode = "gif";
	} elsif ($ARGV[$i] eq "hide") {
		$mode = "hide";
		$giffile = $ARGV[++$i];
		if (!($giffile =~ /\.gif$/i)) {
			exit(1);
		}
		if ($giffile =~ /[<>|&]/) {
			exit(1);
		}
	} elsif ($ARGV[$i] eq "name") {
		$count_name = $ARGV[++$i];
		if ($count_name !~ /^[a-zA-Z0-9]+$/) {
			exit(1);
		}
		$file_count  = "$count_name" . ".cnt";
		$file_date   = "$count_name" . ".dat";
		$file_access = "$count_name" . ".acc";
	} elsif ($ARGV[$i] eq "ref") {
		$reffile = $ARGV[++$i];
	}
}

#
# ���ϐ�TZ����{���Ԃɐݒ肷��
#
$ENV{'TZ'} = "JST-9";

#
# ���b�N���𓾂�
#
if ($do_file_lock) {
	foreach $i ( 1, 2, 3, 4, 5, 6 ) {
		if (mkdir("$file_lock", 0755)) {
			# ���b�N�����B���̏����ցB
			last;
		} elsif ($i == 1) {
			# 10���ȏ�Â����b�N�t�@�C���͍폜����B
			($mtime) = (stat($file_lock))[9];
			if ($mtime < time() - 600) {
				rmdir($file_lock);
			}
		} elsif ($i < 6) {
			# ���b�N���s�B1�b�҂��čăg���C�B
			sleep(1);
		} else {
			# ���x����Ă����b�N���s�B������߂�B
			exit(1);
		}
	}
}

#
# �r���ŏI�����Ă����b�N�t�@�C�����c��Ȃ��悤�ɂ���
#
sub sigexit { rmdir($file_lock); exit(0); }
$SIG{'PIPE'} = $SIG{'INT'} = $SIG{'HUP'} = $SIG{'QUIT'} = $SIG{'TERM'} = "sigexit";

#
# �J�E���^�[�t�@�C������J�E���^�[�l��ǂݏo���B
#
if (open(IN, "< $file_count")) {
	$count = <IN>;
	close(IN);
} else {
	$count = -1;
}

#
# ���t�t�@�C������ŏI�A�N�Z�X���t��ǂݏo���B
#
if (open(IN, "< $file_date")) {
	$date_log = <IN>;
	close(IN);
} else {
	$date_log = "";
}

#
# �����̓��t�𓾂�
#
($sec, $min, $hour, $mday, $mon, $year) = localtime(time());
$date_now = sprintf("%04d/%02d/%02d", 1900 + $year, $mon + 1, $mday);
$time_now = sprintf("%02d:%02d:%02d", $hour, $min, $sec);

#
# ���t���قȂ�A�܂�A�������߂ẴA�N�Z�X�ł����
#
if ($date_log ne $date_now) {

	#
	# �A�N�Z�X���O�����[���ő��M����
	#
	if ($mailto ne "") {
		$tmp_count = 0;
		open(IN, "< $file_access");
		while (<IN>) {
			if (/^COUNT/) {
				$tmp_count++;
			}
		}
		close(IN);
		$msg = "";
		$msg .= "To: $mailto\n";
		if ($mailfrom eq "") {
			$msg .= "From: $count_name\n";
		} else {
			$msg .= "From: $mailfrom\n";
		}
		$msg .= "Subject: ACCESS $date_log $tmp_count\n";
		$msg .= "\n";
		if ($account_detail) {
			open(IN, "< $file_access");
			while (<IN>) {
				$msg .= $_;
			}
			close(IN);
		} else {
			$msg .= "Access = $tmp_count\n";
		}
		open(OUT, "| $sendmail $mailto");
		print OUT $msg;
		close(OUT);
	}

	#
	# �A�N�Z�X���O������������
	#
	open(OUT, "> $file_access");
	close(OUT);

	#
	# �����̓��t����t���O�t�@�C���ɏ����o��
	#
	open(OUT, "> $file_date");
	print(OUT "$date_now");
	close(OUT);
}

#
# ���łɓ��A�h���X����̃A�N�Z�X������΃J�E���g�A�b�v���Ȃ�
#
$count_up = 1;
if ($do_address_check) {
	open(IN, "$file_access");
	while (<IN>) {
		if ($_ eq "ADDR  = [ $ENV{'REMOTE_ADDR'} ]\n") {
			$count_up = 0;
			last;
		}
	}
	close(IN);
}

#
# �J�E���g�A�b�v����
#
if (($count >= 0) && ($count_up == 1)) {

	#
	# �J�E���^���ЂƂC���N�������g����
	#
	$count++;

	#
	# �A�N�Z�X���O���L�^����
	#
	open(OUT, ">> $file_access");

	# �J�E���g
	print(OUT "COUNT = [ $count ]\n");

	# ����
	print(OUT "TIME  = [ $time_now ]\n");

	# IP�A�h���X
	$addr = $ENV{'REMOTE_ADDR'};
	print(OUT "ADDR  = [ $addr ]\n");

	# �z�X�g��
	$host = $ENV{'REMOTE_HOST'};
	if ($do_addr_to_host && (($host eq "") || ($host eq $addr))) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
	}
	if (($host ne "") && ($host ne $addr)) {
		print(OUT "HOST  = [ $host ]\n");
	}

	# �G�[�W�F���g��
	print(OUT "AGENT = [ $ENV{'HTTP_USER_AGENT'} ]\n");

	# �����N��(SSI)
	$referer = $ENV{'HTTP_REFERER'};
	if (($mode eq "text") && ($referer ne "")) {
		if ($do_decode_url eq 1) {
			$referer =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
		}
		print(OUT "REFER = [ $referer ]\n");
	}

	# �����N��(CGI)
	$reffile =~ s/\\//g;
	if ($reffile && (!$my_url || ($reffile !~ /$my_url/))) {
		if ($do_decode_url eq 1) {
			$reffile =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
		}
		print(OUT "FROM  = [ $reffile ]\n");
	}

	print(OUT "\n");
	close(OUT);

	#
	# �J�E���^���J�E���^�t�@�C���ɏ����߂�
	#
	if (open(OUT, "> $file_count")) {
		print(OUT "$count");
		close(OUT);
	}
}

#
# CGI�X�N���v�g�̌��ʂƂ��ăJ�E���^�[�������o��
#
if ($count == -1) {
	$count = 0;
}
if ($figure != 0) {
	$cntstr = sprintf(sprintf("%%0%dld", $figure), $count);
} else {
	$cntstr = sprintf("%ld", $count);
}
if ($mode eq "text") {
	printf("Content-type: text/html\n");
	printf("\n");
	printf("$cntstr\n");
} elsif ($mode eq "gif") {
	printf("Content-type: image/gif\n");
	printf("\n");
	@files = ();
	for ($i = 0; $i < length($cntstr); $i++) {
		$n = substr($cntstr, $i, 1);
		push(@files, "$n.gif");
	}
	require "./gifcat.pl";
	binmode(STDOUT);
	print &gifcat'gifcat(@files);
} elsif ($mode eq "hide") {
	printf("Content-type: image/gif\n");
	printf("\n");
	$size = -s $giffile;
	open(IN, $giffile);
	binmode(IN);
	binmode(STDOUT);
	read(IN, $buf, $size);
	print $buf;
	close(IN);
}

#
# ���b�N�����J������
#
if ($do_file_lock) {
	rmdir($file_lock);
}

#
# CGI���g�p�ł��邩�e�X�g���s���B
#
sub test {
	print "Content-type: text/html\n";
	print "\n";
	print "<html>\n";
	print "<head>\n";
    print "<title>Test</title>\n";
    print "</head>\n";
	print "<body>\n";
	print "<p>OK. CGI�X�N���v�g�͐���ɓ����Ă��܂��B</p>\n";
	if ($mailto ne "") {
		if (! -f $sendmail) {
			print "<p>ERROR: $sendmail �����݂��܂���B</p>\n";
		}
	}
	if (-d $file_lock) {
		print "<p>ERROR: $file_lock ���c���Ă��܂��B</p>\n";
	}
	if (! -r $file_count) {
		print "<p>ERROR: $file_count �����݂��܂���B</p>\n";
	} elsif (! -w $file_count) {
		print "<p>ERROR: $file_count ���������݉\�ł͂���܂���B</p>\n";
	}
	if (! -r $file_date) {
		print "<p>ERROR: $file_date �����݂��܂���B</p>\n";
	} elsif (! -w $file_date) {
		print "<p>ERROR: $file_date ���������݉\�ł͂���܂���B</p>\n";
	}
	if (! -r $file_access) {
		print "<p>ERROR: $file_access �����݂��܂���B</p>\n";
	} elsif (! -w $file_access) {
		print "<p>ERROR: $file_access ���������݉\�ł͂���܂���B</p>\n";
	}
	if (($chdir ne "") && (! -d $chdir)) {
		print "<p>ERROR: $chdir �����݂��܂���B</p>\n";
	}
	print "</body>\n";
	print "</html>\n";
	exit(0);
}

