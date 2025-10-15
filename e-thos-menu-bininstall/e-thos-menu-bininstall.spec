Name:           e-thos-menu
Version:        0.3.0
Release:        2%{?dist}
Summary:        Launcher-driven managers for Linux by e-tho

License:        GPL-3.0-or-later
URL:            https://github.com/e-tho
Source0:        %{url}/bzmenu/releases/download/v%{version}/bzmenu-x86_64-linux-gnu
Source1:        %{url}/iwmenu/releases/download/v%{version}/iwmenu-x86_64-linux-gnu
Source2:        %{url}/pwmenu/releases/download/v%{version}/pwmenu-x86_64-linux-gnu
Source3:        %{url}/bzmenu/releases/download/v%{version}/bzmenu-aarch64-linux-gnu
Source4:        %{url}/iwmenu/releases/download/v%{version}/iwmenu-aarch64-linux-gnu
Source5:        %{url}/pwmenu/releases/download/v%{version}/pwmenu-aarch64-linux-gnu

# Runtime dependencies
Requires:       bluez
Requires:       iwd
Requires:       pipewire
Requires:       dbus

%global debug_package %{nil}
%global __os_install_post %{nil}

%description
bzmenu (BlueZ Menu) manages Bluetooth through your launcher of choice (like rofi, dmenu, or fuzzel).
iwmenu (iNet Wireless Menu) manages Wi-Fi through your launcher of choice.
pwmenu (PipeWire Menu) manages audio through your launcher of choice.
this spec file simply downloads the pre-built executables from github release and puts them into _bindir

%prep

%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}

# 如果构建架构是 x86_64，使用 Source 0-2
%ifarch x86_64
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/bzmenu
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/iwmenu
install -p -m 755 %{SOURCE2} %{buildroot}%{_bindir}/pwmenu
%endif

# 如果构建架构是 aarch64，使用 Source 3-5
%ifarch aarch64
install -p -m 755 %{SOURCE3} %{buildroot}%{_bindir}/bzmenu
install -p -m 755 %{SOURCE4} %{buildroot}%{_bindir}/iwmenu
install -p -m 755 %{SOURCE5} %{buildroot}%{_bindir}/pwmenu
%endif

%files
%defattr(-,root,root,-)
%{_bindir}/bzmenu
%{_bindir}/iwmenu
%{_bindir}/pwmenu

%changelog
* Tur Oct 16 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.3.0-2
- Install binary base on arch.

* Wed Oct 15 2025 jhuang6451 <xplayerhtz123@outlook.com> - 0.3.0-1
- Initial release for v0.3.0.