#-*- coding: utf-8 -*-

{
	"name": "Assets Management",
	"version": "1.0",
	"depends": [
		"base",
		"account",
		"mail",
		"om_account_asset"
	],
	"author": "Dino Herlambang",
	"category": "Utility",
	"website": "https://www.instagram.com/_dinoherlambang_/",
	"images": [
		"static/description/images/main_screenshot.jpg"
	],
	"price": "100",
	"license": "OPL-1",
	"currency": "USD",
	"summary": "Assets Management inheritance and added more features",
	"description": "",
	"data": [
		"security/groups.xml",
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/assets_list.xml",
		"view/assets_category.xml",
		"view/asset_moves.xml",
		"data/sequence_asset_moves.xml",
		"view/asset_location.xml",
		"view/warranty.xml",
		"view/hr_employee.xml",
		"view/res_partner.xml",
		"view/asset_status.xml",
		"report/asset_moves.xml",
		"report/warranty.xml",
		"report/asset_status.xml",
		# "report/asset_label.xml",
		# "report/report.xml"
	],
	"installable": True,
	"auto_install": False,
	"application": True
}