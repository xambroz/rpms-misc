Name:           python-spotdl
Version:        4.0.7
Release:        1%{?dist}
Summary:        Download your Spotify playlists and songs along with album art and metadata

%global pypi_name spotdl
%global pypi_version 4.0.7

License:        None
URL:            https://github.com/spotDL/spotify-downloader/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
<! mdformat-toc start --sluggithub ><! !!! IF EDITING THE README, ENSURE TO
COPY THE WHOLE FILE TO index.md in /docs/ <div align"center"> spotDL v4Download
your Spotify playlists and songs along with album art and metadata[![MIT
License]( [![PyPI version]( ![GitHub commits since latest release (by date)](
}

%description %_description


%package -n     python%{python3_pkgversion}-spotdl
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-}

Requires:       (python3dist(beautifulsoup4) >= 4.11.1 with python3dist(beautifulsoup4) < 5~~)
Requires:       (python3dist(fastapi) < 0.89 or python3dist(fastapi) > 0.89)
Requires:       (python3dist(mutagen) >= 1.46 with python3dist(mutagen) < 2~~)
Requires:       (python3dist(platformdirs) >= 2.6.2 with python3dist(platformdirs) < 3~~)
Requires:       (python3dist(pydantic) >= 1.10.4 with python3dist(pydantic) < 2~~)
Requires:       (python3dist(pykakasi) >= 2.2.1 with python3dist(pykakasi) < 3~~)
Requires:       (python3dist(python-slugify) >= 7 with python3dist(python-slugify) < 8~~)
Requires:       (python3dist(pytube) >= 12.1.2 with python3dist(pytube) < 13~~)
Requires:       (python3dist(rapidfuzz) >= 2.13.7 with python3dist(rapidfuzz) < 3~~)
Requires:       (python3dist(requests) >= 2.28.1 with python3dist(requests) < 3~~)
Requires:       (python3dist(rich) >= 13.0.1 with python3dist(rich) < 14~~)
Requires:       python3dist(setuptools)
Requires:       (python3dist(spotipy) >= 2.22 with python3dist(spotipy) < 3~~)
Requires:       (python3dist(syncedlyrics) >= 0.2.1 with python3dist(syncedlyrics) < 0.3~~)
Requires:       (python3dist(uvicorn) >= 0.20 with python3dist(uvicorn) < 0.21~~)
Requires:       (python3dist(yt-dlp) >= 2023.1.6 with python3dist(yt-dlp) < 2024~~)
Requires:       (python3dist(ytmusicapi) >= 0.22 with python3dist(ytmusicapi) < 0.23~~)
Requires:       (python3dist(ytmusicapi) >= 0.24 with python3dist(ytmusicapi) < 0.25~~)

%description -n python%{python3_pkgversion}-spotdl
<! mdformat-toc start --sluggithub ><! !!! IF EDITING THE README, ENSURE TO
COPY THE WHOLE FILE TO index.md in /docs/ <div align"center"> spotDL v4Download
your Spotify playlists and songs along with album art and metadata[![MIT
License]( [![PyPI version]( ![GitHub commits since latest release (by date)](


%prep
%autosetup -n spotdl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spotdl

%files -n python%{python3_pkgversion}-spotdl -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/spotdl

%changelog
* Wed Feb 01 2023 Michal Ambroz <rebus@seznam.cz> - 4.0.7-1
- Initial package.
