%define	_tname	BlueSteel
Summary:	Enlightenment BlueSteel Theme
Summary(pl):	Wystrój BlueSteel dla enlightenmenta
Name:		enlightenment-theme-%{_tname}
Version:	0.16
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	15b713cb11071116cfb4bedd99853d7a
# Source0-size:	724460
Patch0:		%{name}-i18n.patch
URL:		http://www.enlightenment.org/
Requires:	enlightenment
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment BlueSteel Theme.

%description -l pl
Wystrój BlueSteel dla enlightenmenta.

%prep
%setup -q
mkdir %{_tname}
tar -zxf %{_tname}.etheme -C %{_tname}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/themes/
cp -a %{_tname} $RPM_BUILD_ROOT%{_datadir}/enlightenment/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/themes/%{_tname}
