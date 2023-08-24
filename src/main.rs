use std::io;
use image::{GenericImage, GenericImageView, ImageBuffer, RgbaImage};

fn main() {
    println!("Hello, world!");
}

fn get_image_bounds(img: &dyn GenericImageView<Pixel = RgbaImage>) -> (u32, u32, u32, u32) {
    let (width, height) = img.dimensions();
    return (2,2,2,2);
}
