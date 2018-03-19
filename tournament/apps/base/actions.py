# -*- coding: utf-8 -*-
import csv
import copy
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.template import Context, Template


def copy_object(modeladmin, request, queryset):

    for obj in queryset:
        sd_copy = copy.copy(obj)
        sd_copy.id = None
        sd_copy.save()

copy_object.short_description = _('Make a copy')


def download_report(modeladmin, request, queryset):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)

    queryset = queryset.select_related()
    data = queryset.values()
    writer.writerow(data[0].keys())

    for datum in data:
        writer.writerow([unicode(s).encode("utf-8") for s in datum.values()])

    return response

download_report.short_description = _('Download Report')


def get_csv_from_dict_list(field_list, data):
    csv_line = ";".join(['{{ row.%s|addslashes }}' % field for field in field_list])
    template = "{% for row in data %}" + csv_line + "\n{% endfor %}"
    return Template(template).render(Context({"data": data}))


def export_as_csv(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied

    replace_dc = {'\n': '* ', '\r': '', ';': ',', '\"': '|', '\'': '|', 'True': 'Si', 'False': 'No'}
    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    w = csv.writer(response, delimiter=';')
    # import pdb; pdb.set_trace()
    try:
        field_names = modeladmin.model.get_csv_fields()
        v_field_names = field_names
    except:
        field_names = [field.name for field in opts.fields]
        v_field_names = [getattr(field, 'verbose_name') or field.name for field in opts.fields]
    # print field_names
    v_field_names = map(lambda x: x.encode('utf-8') if x != 'ID' else 'Id', v_field_names)

    w.writerow(v_field_names)
    ax = []
    for obj in queryset:
        acc = {}
        for field in field_names:
            try:
                uf = unicode(getattr(obj, field)()).encode('utf-8')
            except:
                try:
                    uf = unicode(getattr(obj, field)).encode('utf-8')
                except:
                    uf = ''
            for i, j in replace_dc.iteritems():
                uf = uf.replace(i, j)
            if uf == 'None':
                uf = ''
            acc[field] = uf

        ax.append(acc)
    response.write(get_csv_from_dict_list(field_names, ax))
    return response

export_as_csv.short_description = _('Download CVS')
