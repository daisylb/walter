from os import listdir

from . import sources

DEFAULT_SOURCES = (
    sources.EnvironmentSource(),
    sources.IniFileSource(),
)


class SourceList:
    def __init__(self, search_path, sources=None):
        if sources is None:
            sources = DEFAULT_SOURCES

        self.source_list = []

        # This is a little trickier than you'd expect. We mostly want to
        # preserve the order passed in to the constructor, but we also
        # want directory heirachy to be more important i.e. if we have
        # sources=[IniFileSource(), JsonFileSource()] and our search
        # start directory is /foo/bar/baz/ we want
        # /foo/bar/settings.json to override /foo/settings.ini.
        # As a compromise, we iterate through sources and add regular
        # sources to the source list immediately, but collect file
        # meta-sources up and do a path search with them one by one.
        file_sources = []
        for source in sources:
            if isinstance(source, sources.FileSource):
                file_sources.append(source)
            else:
                # clear any file sources first
                if file_sources:
                    self._path_search(file_sources, search_path)
                    file_sources = []
                self.source_list.append(source)
        # clear any file sources at the end of the list
        if file_sources:
            self._path_search(file_sources)

    def _path_search(self, sources, search_path):
        for path in search_path:
            listing = listdir(path)
            for source in sources:
                self.source_list.extend(
                    source.create(x) for x in listing
                    if source.match_filename(x)
                )
