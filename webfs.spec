Summary:	Lightweight HTTP server for static content
Summary(pl):	Lekki serwer HTTP dla statycznych danych
Name:		webfs
Version:	1.21
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.bytesex.org/releases/webfs/%{name}-%{version}.tar.gz
# Source0-md5:	6dc125fe160479404147e7bbfc781dbc
URL:		http://bytesex.org/webfs.html
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple HTTP server for purely static content. You can use it
to serve the content of a FTP server via HTTP for example. It is also
nice to export some files the quick way by starting a http server in a
few seconds, without editing some config file first.

%description -l pl
webfs to prosty serwer HTTP do czysto statycznych danych. Mo¿na go
u¿ywaæ np. do udostêpniania zawarto¶ci serwera FTP po HTTP. Daje
mo¿liwo¶æ ³atwego i szybkiego udostêpnienia plików poprzez
uruchomienie serwera w kilka sekund, bez wcze¶niejszego modyfikowania
ilu¶ plików konfiguracyjnych.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

# to be PLDified
#install webfsd.conf $RPM_BUILD_ROOT/etc/sysconfig/webfsd
#install webfsd.redhat $RPM_BUILD_ROOT%{_initrddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/webfsd
%{_mandir}/man1/webfsd.1*
