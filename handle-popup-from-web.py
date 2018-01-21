main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle
driver.find_element_by_xpath(u'//a[text()="click here"]').click()
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to.window(signin_window_handle)
driver.find_element_by_xpath(u'//input[@id="id_1"]').send_keys(user_text_1)
driver.find_element_by_xpath(u'//input[@value="OK"]').click()
driver.find_element_by_xpath(u'//input[@id="id_2"]').send_keys(user_text_2)
driver.find_element_by_xpath(u'//input[@value="OK"]').click()
driver.switch_to.window(main_window_handle) #or driver.switch_to_default_content()
