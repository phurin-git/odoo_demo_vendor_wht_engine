FROM odoo:18

USER root

# copy custom module into extra addons
COPY . /mnt/extra-addons/demo_vendor_wht_engine

USER odoo
