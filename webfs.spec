Summary:	Lightweight HTTP server for static content
Summary(pl):	Lekki serwer HTTP dla statycznych danych
Name:		webfs
Version:	1.19
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://bytesex.org/misc/%{name}_%{version}.tar.gz
URL:		http://bytesex.org/webfs.html
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple HTTP server for purely static content. You can use it
to serve the content of a ftp server via http for example. It is also
nice to export some files the quick way by starting a http server in a
few seconds, without editing some config file first.

%description -l pl
webfs to prosty serwer HTTP do czysto statycznych danych. Mo�na go
u�ywa� np. do udost�pniania zawarto�ci serwera ftp po http. Daje
mo�liwo�� �atwego i szybkiego udost�pnienia plik�w poprzez
uruchomienie serwera w kilka sekund, bez wcze�niejszego modyfikowania 
ilu� plik�w konfiguracyjnych.

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
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1

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