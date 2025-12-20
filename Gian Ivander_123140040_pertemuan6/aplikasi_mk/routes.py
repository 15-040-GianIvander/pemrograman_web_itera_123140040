def includeme(config):
    config.add_route('matakuliah_list', '/api/matakuliah')
    config.add_route('matakuliah_detail', '/api/matakuliah/{id}')
