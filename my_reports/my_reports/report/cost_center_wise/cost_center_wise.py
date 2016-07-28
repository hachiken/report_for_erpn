# Copyright (c) 2013, h@ci and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe	
from frappe import _

def execute(filters=None):
	columns = [
		_("Account") + ":Link/Account:140",
		_("Posting Date") + ":Date:100",
		_("Credit") + ":Currency:100",
		_("Debit") + ":Currency:100",
		_("Remarks") + "::400",]
	data = frappe.db.sql("""
		select
		    account, posting_date, credit, debit, remarks
		from
		    `tabGL Entry`
		where
		    cost_center IS NOT NULL AND posting_date>"%s" AND posting_date<"%s"
			""" % (filters["from_date"], filters["to_date"]))
	
	return columns, data