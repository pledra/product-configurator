import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-product-configurator",
    description="Meta package for oca-product-configurator Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-product_configurator',
        'odoo14-addon-product_configurator_mrp',
        'odoo14-addon-product_configurator_purchase',
        'odoo14-addon-product_configurator_sale',
        'odoo14-addon-product_configurator_sale_mrp',
        'odoo14-addon-website_product_configurator',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
