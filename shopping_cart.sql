-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-01-24 08:36:49
-- 伺服器版本： 10.4.22-MariaDB
-- PHP 版本： 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `shopping_cart`
--

-- --------------------------------------------------------

--
-- 資料表結構 `product_list`
--

CREATE TABLE `product_list` (
  `id` int(11) NOT NULL,
  `product` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `cost` int(10) NOT NULL,
  `inventory` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --
-- -- 資料表結構 `User`
-- --
-- CREATE TABLE `User` (
--   `id` int(11) NOT NULL,
--   `username` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
--   `account_number` varchar(16) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
--   `password` varchar(16) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
-- ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- 傾印資料表的資料 `product_list`
--

INSERT INTO `product_list` (`id`, `product`, `cost`, `inventory`) VALUES
(1, '防曬乳', '255', '500'),
(2, '洗髮精', '115', '200'),
(3, '沐浴乳', '99', '155'),
(4, '潤髮乳', '200', '30');

-- --
-- -- 傾印資料表的資料 `User`
-- --

-- INSERT INTO `User` (`id`, `username`, `account_number`, `password`) VALUES
-- (1, 'root', 'root', 'root109321024');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `product_list`
--
ALTER TABLE `product_list`
  ADD PRIMARY KEY (`id`);


-- --
-- -- 資料表索引 `User`
-- --
-- ALTER TABLE `User`
--   ADD PRIMARY KEY (`id`);



--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `product_list`
--
ALTER TABLE `product_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

-- --
-- -- 使用資料表自動遞增(AUTO_INCREMENT) `User`
-- --
-- ALTER TABLE `User`
--   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
-- COMMIT;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
