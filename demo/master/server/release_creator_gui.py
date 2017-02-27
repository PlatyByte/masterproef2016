# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Release", pos = wx.DefaultPosition, size = wx.Size( 532,484 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Package" ), wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer2.Add( self.m_staticText10, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.package_name = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.package_name, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer2.Add( self.m_staticText11, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.package_version = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.package_version, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer2.Add( self.m_staticText13, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.package_description = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.package_description, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer2.Add( self.m_staticText14, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		package_typeChoices = [ u"Executable", u"Zip" ]
		self.package_type = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, package_typeChoices, 0 )
		fgSizer2.Add( self.package_type, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.package_directory = wx.DirPickerCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer2.Add( self.package_directory, 0, wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		
		fgSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.is_framework_check = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Framework", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.is_framework_check, 0, wx.ALL, 5 )
		
		self.is_optional_check = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Optional", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.is_optional_check, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button4 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button4, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer2.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button5 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer1, 0, wx.ALL|wx.EXPAND, 2 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Installer" ), wx.VERTICAL )
		
		fgSizer21 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer21.Add( self.m_staticText8, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.installer_name = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.installer_name, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer21.Add( self.m_staticText9, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.installer_version = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.installer_version, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText101 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		fgSizer21.Add( self.m_staticText101, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.installer_directory = wx.DirPickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer21.Add( self.installer_directory, 0, wx.ALL, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button7 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button7, 0, wx.ALL, 5 )
		
		
		fgSizer21.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button8 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Release", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button8, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		fgSizer21.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		
		sbSizer2.Add( fgSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_treeCtrl1 = wx.TreeCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer5.Add( self.m_treeCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.select_package )
		self.m_button5.Bind( wx.EVT_BUTTON, self.submit_package )
		self.m_button6.Bind( wx.EVT_BUTTON, self.clear_package )
		self.m_button7.Bind( wx.EVT_BUTTON, self.select_installer )
		self.m_button8.Bind( wx.EVT_BUTTON, self.release_installer )
		self.m_button9.Bind( wx.EVT_BUTTON, self.clear_installer )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def select_package( self, event ):
		event.Skip()
	
	def submit_package( self, event ):
		event.Skip()
	
	def clear_package( self, event ):
		event.Skip()
	
	def select_installer( self, event ):
		event.Skip()
	
	def release_installer( self, event ):
		event.Skip()
	
	def clear_installer( self, event ):
		event.Skip()
	

