from pyramid.view import view_config
from pyramid.response import Response
from ..models import Matakuliah
import json


# GET semua matakuliah
@view_config(route_name='matakuliah_list', request_method='GET', renderer='json')
def get_all_matakuliah(request):
    data = request.dbsession.query(Matakuliah).all()
    return [mk.to_dict() for mk in data]


# GET detail matakuliah
@view_config(route_name='matakuliah_detail', request_method='GET', renderer='json')
def get_matakuliah(request):
    mk_id = int(request.matchdict['id'])
    mk = request.dbsession.query(Matakuliah).get(mk_id)

    if not mk:
        return Response(
            json.dumps({'error': 'Matakuliah tidak ditemukan'}),
            status=404,
            content_type='application/json'
        )

    return mk.to_dict()


# POST tambah matakuliah
@view_config(route_name='matakuliah_list', request_method='POST', renderer='json')
def create_matakuliah(request):
    data = request.json_body

    mk = Matakuliah(
        kode_mk=data['kode_mk'],
        nama_mk=data['nama_mk'],
        sks=data['sks'],
        semester=data['semester']
    )

    request.dbsession.add(mk)
    request.dbsession.commit()

    return {'message': 'Matakuliah berhasil ditambahkan'}


# PUT update matakuliah
@view_config(route_name='matakuliah_detail', request_method='PUT', renderer='json')
def update_matakuliah(request):
    mk_id = int(request.matchdict['id'])
    data = request.json_body

    mk = request.dbsession.query(Matakuliah).get(mk_id)
    if not mk:
        return Response(
            json.dumps({'error': 'Matakuliah tidak ditemukan'}),
            status=404,
            content_type='application/json'
        )

    mk.kode_mk = data['kode_mk']
    mk.nama_mk = data['nama_mk']
    mk.sks = data['sks']
    mk.semester = data['semester']

    request.dbsession.commit()

    return {'message': 'Matakuliah berhasil diupdate'}


# DELETE hapus matakuliah
@view_config(route_name='matakuliah_detail', request_method='DELETE', renderer='json')
def delete_matakuliah(request):
    mk_id = int(request.matchdict['id'])
    mk = request.dbsession.query(Matakuliah).get(mk_id)

    if not mk:
        return Response(
            json.dumps({'error': 'Matakuliah tidak ditemukan'}),
            status=404,
            content_type='application/json'
        )

    request.dbsession.delete(mk)
    request.dbsession.commit()

    return {'message': 'Matakuliah berhasil dihapus'}
